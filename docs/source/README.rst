TEST
=====
<section id="sostrades-dev-tools-setup-sostrades-platform">
<h1>sostrades-dev-tools : Setup SoStrades platform</h1>
<p>This repository contains files for local platform deployment, and local for virtual environment venv creation. It also contains default vscode workspace configuration files.</p>
<section id="choose-your-environment">
<h2>1. Choose your environment</h2>
<p>Depending on your needs, two different environment installations are proposed. A common setup is mandatory whatever the installation you need to perform.</p>
<p>Follow the diagram below to know what you need to install:</p>
<p><img alt="" src="doc_images/choose_your_env.png" /></p>
</section>
<section id="common-setup">
<h2>2. Common Setup</h2>
<p>The objective is to have all folders properly organized on your local computer. Admin rights on your computer are mandatory to ensure a smooth installation process.</p>
<section id="wsl-and-or-ubuntu-install-conda">
<h3>2.1 WSL and/or Ubuntu install + Conda</h3>
<ol class="arabic simple">
<li><p>Install WSL2 if using Windows</p></li>
</ol>
<pre class="code literal-block"><code>wsl --install --web-download
</code></pre>
<ol class="arabic simple" start="2">
<li><p>Install Ubuntu 22.04 LTS</p></li>
</ol>
<p>On Windows with WSL2</p>
<pre class="code literal-block"><code>wsl --install -d Ubuntu-22.04
</code></pre>
<p>As an alternative
You may use directly Ubuntu 22.04 LTS or an equivalent, in this case you may have to make some changes on you own.</p>
<ol class="arabic simple" start="4">
<li><p>Launch Ubuntu</p></li>
</ol>
<p><img alt="" src="doc_images/ubuntu_installed.png" /></p>
<ol class="arabic simple" start="5">
<li><p>Conda installation
Check conda installation with
<span class="docutils literal">conda info</span>, if not installed do</p></li>
</ol>
<pre class="code literal-block"><code>pip install conda
</code></pre>
<p>or</p>
<pre class="code literal-block"><code>wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
chmod +x Anaconda3-2023.09-0-Linux-x86_64.sh
./Anaconda3-2023.09-0-Linux-x86_64.sh
# =&gt; Accept licence and follow instructions
# Restart terminal for env variables update
</code></pre>
<ol class="arabic simple" start="6">
<li><p>Install jq</p></li>
</ol>
<pre class="code literal-block"><code>$ sudo apt  install jq           #For Debian/Ubuntu
$ sudo yum install jq            #For Fedora/CentOS/RHEL
$ sudo pacman -Syu jq            #For Arch
</code></pre>
</section>
<section id="clone-code-and-tools">
<h3>2.3 Clone code and tools</h3>
<p>All development environments are built from a dedicated directory initiated with this repository. This directory will be used as root and will contains all the others necessary repositories from OS-Climate. This root directory contains VSCode tasks and launch docker-compose files. This allows to launch SoStrades in docker containers and to debug webapi servers directly from thus container in VS Code. From the repository a script is available to clone all the repositories to prepare the development environment.</p>
<ol class="arabic simple">
<li><p>Clone this repository in root directory</p></li>
</ol>
<pre class="code literal-block"><code>git clone https://github.com/os-climate/sostrades-dev-tools
(For SSH : git clone git&#64;github.com:os-climate/sostrades-dev-tools.git)
 
cd sostrades-dev-tools
</code></pre>
<ol class="arabic simple" start="2">
<li><p>If needed configure model repositories : Edit the model_repositories.json and platform_repositories.json according to what repositories you want.</p></li>
</ol>

<ol class="arabic simple" start="3">
<li><p>Launch the PrepareDevEnv.sh</p></li>
</ol>
<pre class="code literal-block"><code>./PrepareDevEnv.sh  (if necessary sudo chmod +x PrepareDevEnv.sh to allow execution rights)

</code></pre>
</section>
</section>
<section id="local-docker-env-installation">
<h2>3. Local Docker Env Installation</h2>
<p>You are a developer and need a local working platform.</p>
<section id="prerequisites">
<h3>3.1 Prerequisites</h3>
<p>Follow common setup paragraph :</p>
<ul class="simple">
<li><p>WSL2 + Ubuntu 22.04 LTS or directly an Ubuntu equivalent</p></li>
</ul>
<p>You will need also:</p>
<ul class="simple">
<li><p>Docker 24.0.4 installed and running with your account (on Ubuntu)</p></li>
<li><p>Docker compose 2.17.2 installed (on Ubuntu)</p></li>
</ul>
<ol class="arabic simple">
<li><p>Try running  &quot;docker&quot; and  &quot;docker compose&quot; to see if command is recognized</p></li>
</ol>
<pre class="code literal-block"><code>docker --version
docker compose --version 

docker ps 
</code></pre>
<p>If this commands are not working fix docker and docker-compose installation before to continue</p>
</section>
<section id="visual-studio-code-vscode-installation">
<h3>3.2 Visual Studio Code (VSCode) installation</h3>
<p>VSCode settings have been written in dedicated files during execution of PrepareDevEnv.sh (in a previous step).</p>
<p>The following command can be run to install VSCode :</p>
<pre class="code literal-block"><code>sudo snap install --classic code
</code></pre>
<p>In order to benefit from VSCode settings, type the following command in the &quot;sostrades-dev-tools&quot; directory, at the same level than the &quot;./vscode&quot; (hidden) folder (or models/ and platform/ visible directories) :</p>
<pre class="code literal-block"><code>code . &amp;
</code></pre>
</section>
<section id="prepare-development-environment-with-docker">
<h3>3.3 Prepare development environment with docker</h3>
<p>All the commands below need to be done from the root directory.</p>
<ol class="arabic simple">
<li><p>Build all docker images</p></li>
</ol>
<pre class="code literal-block"><code>docker compose build
</code></pre>
</section>
<section id="start-and-play-with-your-sostrades-gui">
<h3>3.4 Start and play with your SoSTrades GUI</h3>
<p>Here all commands needed to play with the image built are listed :</p>
<ul class="simple">
<li><p>First start of your local GUI instance</p></li>
</ul>
<pre class="code literal-block"><code>docker compose up
</code></pre>
<p>Wait some minutes</p>
<p>Go to <a href="#system-message-1"><span class="problematic" id="problematic-1"></span></a> with your web browser and connect with the following credentials :</p>
<p>login : user</p>
<p>password : mdp</p>
<ul class="simple">
<li><p>Stop the instance</p></li>
</ul>
<pre class="code literal-block"><code>docker compose stop
</code></pre>
<ul class="simple">
<li><p>Restart the instance</p></li>
</ul>
<pre class="code literal-block"><code>docker compose start
</code></pre>
<ul class="simple">
<li><p>Clean the instance (if errors)</p></li>
</ul>
<pre class="code literal-block"><code>docker compose down
</code></pre>
<ul class="simple">
<li><p>Start the application with debug mode</p></li>
</ul>
<pre class="code literal-block"><code>docker compose -f docker-compose.debug.yml up
</code></pre>
<p>If using VSCode you will find  4 debug profiles :</p>
<ul class="simple">
<li><p>Remote attach main</p></li>
<li><p>Remote attach message</p></li>
<li><p>Remote attach post processing</p></li>
<li><p>Remote attach data</p></li>
</ul>
<p><img alt="" src="doc_images/vscode_debug_mode.png" /></p>
<p>After having launched each debug profile your application should be available on 127.0.0.1:1080 and you will be able to debug it directly running in the container and from VSCode. All debug profiles must be started since flask api are waiting for debug connection to continue. Then without debug connections platform won't be responding.</p>
</section>
<section id="useful-links">
<h3>3.5 Useful links</h3>
<p>https://code.visualstudio.com/docs/containers/docker-compose</p>
<p>https://code.visualstudio.com/docs/containers/debug-common</p>
</section>
</section>
<section id="local-model-development-env-installation">
<h2>4. Local Model Development Env Installation</h2>
<p>The objective is to have a working local dev environment based on a conda venv, with pre-configured VS-CODE workspace to be able to run code and debug. Other IDE may be used but should be configured properly.</p>
<section id="prerequisites-1">
<h3>4.1 Prerequisites</h3>
<p>Follow 2. common setup paragraph :</p>
<ul class="simple">
<li><p>WSL2 + Ubuntu 22.04 LTS or directly an Ubuntu equivalent</p></li>
<li><p>Conda installed</p></li>
</ul>
</section>
<section id="prepare-conda-environment">
<h3>4.2 Prepare Conda environment</h3>
<pre class="code literal-block"><code>./PrepareCondaEnv.sh  (if necessary sudo chmod +x PrepareCondaEnv.sh to allow execution rights)
</code></pre>
</section>
<section id="visual-studio-code-vscode-installation-1">
<h3>4.3 Visual Studio Code (VSCode) installation</h3>
<p>VSCode settings have been written in dedicated files during execution of PrepareDevEnv.sh (in a previous step).</p>
<p>The following command can be run to install VSCode :</p>
<pre class="code literal-block"><code>sudo snap install --classic code
</code></pre>
<p>In order to benefit from VSCode settings, type the following command in the &quot;sostrades-dev-tools&quot; directory, at the same level than the &quot;./vscode&quot; (hidden) folder (or models/ and platform/ visible directories) :</p>
<pre class="code literal-block"><code>code . &amp;
</code></pre>
</section>
<section id="use-conda-env-in-vs-code">
<h3>4.4 Use conda env in VS code</h3>
<p>Use keys windows + shift + p to open command panel, search for &quot;Python: Select Interpreter&quot;</p>
<p><img alt="" src="doc_images/select_interpreter.png" /></p>
<p>Select &quot;Python 3.9.x (&quot;SOSTradesEnv&quot;)</p>
<p><img alt="" src="doc_images/select_python.png" /></p>
<p>Now you can launch any SoSTrades code from VSCode.</p>
</section>
</section>
</section>
<section class="system-messages">
<h1>Docutils System Messages</h1>
<aside class="system-message" id="system-message-1">
<p class="system-message-title">System Message: ERROR/3 (<span class="docutils literal">README.md</span>, line 155); <em><a href="#problematic-1">backlink</a></em></p>
<p>Unknown target name: &quot;127.0.0.1:1080&quot;.</p>
</aside>
</section>
