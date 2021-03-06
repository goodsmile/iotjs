# Copyright 2016-present Samsung Electronics Co., Ltd. and other contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

class Platform(object):
    def __init__(self):
        if sys.platform == "win32":
            _os = "windows"
            _arch = "i686" # TODO: allow x86_64 also
        else:
            _os, _, _, _, _arch = os.uname()
        self._os = _os
        self._arch = _arch

    def os(self):
        """ Retrieve host OS name. """
        return self._os.lower()

    def arch(self):
        """ Retrieve host arch name. """
        arch = self._arch.lower()
        if arch in ["armv7l"]:
            arch = "arm"
        return arch
