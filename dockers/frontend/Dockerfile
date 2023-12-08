# Copyright 2023 Capgemini

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------
# Stage 1 : Distribution building
FROM node:12.16.1 as front_build

#------------------------------------------------------------------------------
# Extract source code 'sostrades-webgui'
COPY  ./platform/sostrades-webgui /tmp/node_build/sostrades-webgui/
#------------------------------------------------------------------------------
# Remove question about analytics
RUN export NG_CLI_ANALYTICS=off

WORKDIR /tmp/node_build/sostrades-webgui/

#------------------------------------------------------------------------------
# Install project package and build distribution
RUN npm install
RUN node_modules/@angular/cli/bin/ng build --prod

#------------------------------------------------------------------------------
# Stage 2 : Final image buiding with NGINX webserver
FROM nginx:latest

#------------------------------------------------------------------------------
# Transfer wbesite distribution from previous image to this new one
COPY --from=front_build /tmp/node_build/sostrades-webgui/dist/sos-trades-gui /usr/share/nginx/html

#------------------------------------------------------------------------------
# Transfer nginx configuration
COPY ./../dockers/frontend/conf/nginx.conf /etc/nginx/nginx.conf

