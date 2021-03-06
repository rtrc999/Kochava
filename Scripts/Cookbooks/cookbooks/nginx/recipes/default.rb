# Copyright:: 2018, The Authors, All Rights Reserved.
#
# Cookbook Name:: nginx
# Recipe:: plus_package
# Author:: Chenna Vemula <chennarao.py@gmail.com>
#
# Copyright 2008-2013, Chef Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# include_recipe "yum"

package "nginx" do
version "1.6.2"
action :install
end

# template "nginx.conf" do
# source "nginx.conf.erb"
# path "#{node['nginx']['dir']}/nginx.conf"
# action :create
# mode 0644
# end
#
# template "default.conf" do
# source "default-site.erb"
# path "#{node['nginx']['dir']}/conf.d/default.conf"
# action :create
# mode 0644
# end

service "nginx" do
supports :restart => :true
action [:enable, :start]
end
