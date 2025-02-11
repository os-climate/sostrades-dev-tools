"""
Copyright 2024 Capgemini
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
StartSOSTrades.py is a script that run api server, ontology server, and webgui server with venv and node
"""
import os
import queue
import subprocess
import threading
import tkinter as tk
from tkinter import ttk

import psutil
from constants import (
    node_version,
    nvs_cmd_path,
    platform_path,
    sostrades_dev_tools_path,
    venv_script_activate_command,
    venv_script_activate_path,
)
from PIL import Image, ImageTk


class CommandWindow:
    def __init__(
        self, command, name, working_dir, tag=None, depends_on=None, debug_option=False
    ):
        self.debug_option = debug_option
        self.debug_mode = tk.BooleanVar(value=False)
        self.command = command
        self.name = name
        self.working_dir = working_dir
        self.tag = tag
        self.depends_on = depends_on if depends_on else []
        self.process = None
        self.output_queue = queue.Queue()
        self.status = "Idle"
        self.terminated = False
        self.completed = False
        self.memory_usage = "N/A"
        self.auto_scroll = tk.BooleanVar(value=True)  # Default to True

    def launch(self, command_windows):
        if self.status != "Running" and not self.completed:
            # Check dependencies
            for dep_tag in self.depends_on:
                dep_window = next(
                    (cw for cw in command_windows if cw.tag == dep_tag), None
                )
                if dep_window and not dep_window.completed:
                    self.output_queue.put(f"[INFO] Waiting for dependency: {dep_tag}\n")
                    return False

            self.terminated = False

            def run_command():
                self.status = "Running"
                self.output_queue.put("[INFO] STARTING PROCESS\n")
                try:
                    cmd = self.command
                    if self.debug_option and self.debug_mode.get():
                        cmd = "set FLASK_DEBUG=1 && " + cmd
                        cmd += " --debug"  # Add debug flag if debug mode is enabled
                    self.process = subprocess.Popen(
                        cmd,
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        text=True,
                        cwd=self.working_dir,
                        bufsize=1,
                        universal_newlines=True,
                    )
                    while True:
                        line = self.process.stdout.readline()
                        if not line and self.process.poll() is not None:
                            break
                        if self.terminated:
                            break
                        self.output_queue.put(line)

                        # Update memory usage
                        if self.process:
                            try:
                                process = psutil.Process(self.process.pid)
                                self.memory_usage = f"{process.memory_info().rss / (1024 * 1024):.2f} MB"
                            except psutil.NoSuchProcess:
                                self.memory_usage = "N/A"

                    if not self.terminated:
                        self.process.stdout.close()
                        self.process.wait()
                        self.completed = True
                finally:
                    if not self.terminated:
                        self.status = "Completed" if self.completed else "Idle"

            thread = threading.Thread(target=run_command)
            thread.start()
            return True
        return False

    def kill(self):
        if self.process:
            self.output_queue.put("[INFO] TERMINATING PROCESS\n")
            self.terminated = True
            self.completed = False
            try:
                parent = psutil.Process(self.process.pid)
                for child in parent.children(recursive=True):
                    child.terminate()
                parent.terminate()
                parent.wait(5)  # Wait for 5 seconds
            except psutil.NoSuchProcess:
                pass
            except psutil.TimeoutExpired:
                # If termination doesn't work, try to kill forcefully
                for child in parent.children(recursive=True):
                    child.kill()
                parent.kill()
            finally:
                self.status = "Killed"
                self.process = None

        self.memory_usage = "N/A"

    def relaunch(self, command_windows):
        self.kill()
        return self.launch(command_windows)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SoSTrades Local Server Manager")
        self.geometry("1000x600")
        self.configure(bg="#f0f0f0")
        self.update_interval = 5000  # Update every 5 seconds

        # Create a frame for buttons and logos
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Create a frame for buttons (left side)
        self.button_frame = ttk.Frame(self.top_frame)
        self.button_frame.pack(side="left")

        # Add "Launch All" button
        self.launch_all_button = ttk.Button(
            self.button_frame, text="Launch All", command=self.launch_all
        )
        self.launch_all_button.pack(side="left", padx=(0, 5))

        # Add "Kill All" button
        self.kill_all_button = ttk.Button(
            self.button_frame, text="Kill All", command=self.kill_all
        )
        self.kill_all_button.pack(side="left")

        # Create a frame for logos (right side)
        self.logo_frame = ttk.Frame(self.top_frame)
        self.logo_frame.pack(side="right")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=(0, 10))

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.command_windows = []

        # Bind the closing event
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # self.add_logo("CAP.PA_BIG.png")

    def add_logo(self, image_path, max_size=(500, 50)):
        try:
            # Use the image path directly, relative to the script's location
            script_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(script_dir, image_path)

            # Open the image file
            img = Image.open(full_path)

            # Open the image file
            img = Image.open(full_path)

            # Calculate the resize ratio
            ratio = min(max_size[0] / img.width, max_size[1] / img.height)
            new_size = (int(img.width * ratio), int(img.height * ratio))

            # Resize the image
            img = img.resize(new_size, Image.LANCZOS)

            # Convert the image for Tkinter
            tk_img = ImageTk.PhotoImage(img)

            # Create a label with the image
            label = ttk.Label(self.logo_frame, image=tk_img)
            label.image = tk_img  # Keep a reference to avoid garbage collection
            label.pack(side="left", padx=5)
        except Exception as e:
            print(f"Error loading logo {image_path}: {e}")

    def add_command(
        self, command, name, working_dir, tag=None, depends_on=None, debug_option=False
    ):
        cmd_window = CommandWindow(
            command, name, working_dir, tag, depends_on, debug_option
        )
        self.command_windows.append(cmd_window)

        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=name)

        # Create a frame for status light, buttons, and status label
        control_frame = ttk.Frame(frame)
        control_frame.pack(fill="x", padx=5, pady=5)

        # Add buttons side by side
        button_width = 10
        ttk.Button(
            control_frame,
            text="Launch",
            command=lambda: self.launch_command(cmd_window),
            width=button_width,
        ).pack(side="left", padx=2)
        ttk.Button(
            control_frame, text="Kill", command=cmd_window.kill, width=button_width
        ).pack(side="left", padx=2)
        ttk.Button(
            control_frame,
            text="Relaunch",
            command=lambda: self.relaunch_command(cmd_window),
            width=button_width,
        ).pack(side="left", padx=2)

        # Add debug mode checkbox if debug option is available
        if cmd_window.debug_option:
            ttk.Checkbutton(
                control_frame,
                text="Auto relaunch",
                variable=cmd_window.debug_mode,
            ).pack(side="left", padx=5)

        # Add auto-scroll checkbox
        ttk.Checkbutton(
            control_frame,
            text="Auto-scroll",
            variable=cmd_window.auto_scroll,
        ).pack(side="left", padx=5)

        # Modify the status label to include memory usage
        status_label = ttk.Label(control_frame, text="Status: Idle | Memory: N/A")
        status_label.pack(side="right", padx=5)

        # Add status light
        status_light = tk.Label(control_frame, text="●", font=("Arial", 16))
        status_light.pack(side="right", padx=(0, 5))

        # Add text area for output with scrollbar
        output_frame = ttk.Frame(frame)
        output_frame.pack(expand=True, fill="both", padx=5, pady=5)

        output_text = tk.Text(
            output_frame,
            wrap=tk.WORD,
            bg="#1e1e1e",
            fg="#d4d4d4",
            font=("Consolas", 10),
        )
        output_text.pack(side="left", expand=True, fill="both")

        scrollbar = ttk.Scrollbar(
            output_frame, orient="vertical", command=output_text.yview
        )
        scrollbar.pack(side="right", fill="y")
        output_text.configure(yscrollcommand=scrollbar.set)

        # Function to update output and status
        def update_output_and_status():
            while not cmd_window.output_queue.empty():
                line = cmd_window.output_queue.get()
                output_text.insert(tk.END, line)
                if (
                    cmd_window.auto_scroll.get()
                ):  # Only auto-scroll if checkbox is checked
                    output_text.see(tk.END)
            status_label.config(
                text=f"Status: {cmd_window.status} | Memory: {cmd_window.memory_usage}"
            )

            # Update status light
            if cmd_window.status == "Running":
                status_light.config(fg="green")
            elif cmd_window.status == "Killed":
                status_light.config(fg="red")
            else:
                status_light.config(fg="yellow")

            self.after(100, update_output_and_status)

        update_output_and_status()

        # Schedule periodic memory usage updates
        self.update_memory_usage(cmd_window, status_label)

    def update_memory_usage(self, cmd_window, status_label):
        status_label.config(
            text=f"Status: {cmd_window.status} | Memory: {cmd_window.memory_usage}"
        )
        self.after(
            self.update_interval,
            lambda: self.update_memory_usage(cmd_window, status_label),
        )

    def launch_command(self, cmd_window):
        cmd_window.launch(self.command_windows)

    def relaunch_command(self, cmd_window):
        cmd_window.relaunch(self.command_windows)

    def launch_all(self):
        launched = set()
        while len(launched) < len(self.command_windows):
            for cmd_window in self.command_windows:
                if cmd_window not in launched and cmd_window.launch(
                    self.command_windows
                ):
                    launched.add(cmd_window)

    def kill_all(self):
        for cmd_window in self.command_windows:
            cmd_window.kill()

    def on_closing(self):
        self.kill_all()
        self.destroy()

    def run(self):
        # Launch all commands automatically
        self.after(1000, self.launch_all)  # Launch after 3 second delay

        # Start the main event loop
        self.mainloop()


if __name__ == "__main__":
    app = Application()

    if os.path.exists(venv_script_activate_path):
        if os.path.exists(f"{platform_path}/sostrades-webapi"):
            # Perform DB upgrade and Init Process
            app.add_command(
                f"{venv_script_activate_command} && flask db upgrade",
                "DB Upgrade",
                f"{platform_path}/sostrades-webapi",
                tag=["db_upgrade"],
            )
            app.add_command(
                f"{venv_script_activate_command} && flask init_process",
                "Init Process",
                f"{platform_path}/sostrades-webapi",
                tag=["init_process"],
                depends_on=["db_upgrade"],
            )

            # Start sostrades-webapi servers with .venv
            app.add_command(
                f"{venv_script_activate_command} && python server_scripts/split_mode/launch_server_post_processing.py",
                "Post Processing",
                f"{platform_path}/sostrades-webapi",
                depends_on=["init_process"],
                debug_option=True,
            )
            app.add_command(
                f"{venv_script_activate_command} &&  python server_scripts/split_mode/launch_server_main.py",
                "Main",
                f"{platform_path}/sostrades-webapi",
                depends_on=["init_process"],
                debug_option=True,
            )
            app.add_command(
                f"{venv_script_activate_command} &&  python server_scripts/split_mode/launch_server_data.py",
                "Data Server",
                f"{platform_path}/sostrades-webapi",
                depends_on=["init_process"],
                debug_option=True,
            )
            app.add_command(
                f"{venv_script_activate_command} &&  python server_scripts/launch_server_message.py",
                "Message Server",
                f"{platform_path}/sostrades-webapi",
                depends_on=["init_process"],
            )

        else:
            print(f"{platform_path}/sostrades-webapi repository not found")

        if os.path.exists(f"{platform_path}/sostrades-ontology"):
            # Start sostrades-ontology with .venv
            app.add_command(
                f"{venv_script_activate_command} &&  python sos_ontology/rest_api/api.py",
                "REST API",
                f"{platform_path}/sostrades-ontology",
                depends_on=["init_process"],
            )
        else:
            print(f"{platform_path}/sostrades-ontology repository not found")

        os.chdir(sostrades_dev_tools_path)
    else:
        print("Virtual environment (.venv) is not installed")

    if os.path.exists(nvs_cmd_path):
        if os.path.exists(f"{platform_path}/sostrades-webgui"):
            app.add_command(
                f"{nvs_cmd_path} use {node_version} &&   npm start",
                "GUI",
                f"{platform_path}/sostrades-webgui",
                depends_on=["init_process"],
            )
        else:
            print(f"{platform_path}/sostrades-webgui repository not found")
    else:
        print("NVS is not installed")

    app.run()
