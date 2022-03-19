#!/usr/bin/env python

#   Copyright 2017 Federico Cerchiari <federicocerchiari@gmail.com>
#
#   this file is part of emapi
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from setuptools import setup

from emapi import __version__

long_description = """"""

setup(
	name="emapi",
	version=__version__,
	author="Federico Cerchiari",
	author_email="federicocerchiari@gmail.com",
	description="Event-Models based api framework",
	license="APACHE 2.0",
	packages=["emapi"],
	url="https://github.com/Hrabal/Emapi",
	keywords=["python3", "api", "html", "web", "framework"],
	download_url="https://github.com/Hrabal/Emapi/archive/%s.tar.gz" % __version__,
	python_requires=">=3.3",
	long_description=long_description,
	install_requires=["mistune",],
)
