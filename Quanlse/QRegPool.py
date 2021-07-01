#!/usr/bin/python3
# -*- coding: utf8 -*-

# Copyright (c) 2021 Baidu, Inc. All Rights Reserved.
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

"""
Quantum Register Pool
"""
from typing import Dict, TYPE_CHECKING


class QRegStorage:
    """
    The storage for quantum register.
    """

    def __init__(self, index: int, env: 'Scheduler') -> None:
        """
        The quantum register object needs to have an index and a quantum environment.

        :param index: the quantum register index
        :param env: quantum environment or procedure
        :return: None
        """

        self.index = index
        self.env = env


class QRegPool:
    """
    The quantum register dict
    """

    def __init__(self, env: 'Scheduler') -> None:
        """
        The constructor of the QRegPool class

        :param env: the related quantum environment or procedure
        :return: None
        """

        # the quantum environment related with the quantum register dict
        self.env = env
        # the inner data for quantum register dict
        self.registerMap = {}  # type: Dict[int, QRegStorage]

    def __getitem__(self, index: int) -> QRegStorage:
        """
        Return the quantum register at the given index

        :param index: item index
        :return: the returned item
        """
        return self._get(index)

    def __call__(self, index: int) -> QRegStorage:
        """
        Return the quantum register at the given index

        :param index: item index
        :return: the returned quantum register
        """
        return self._get(index)

    def _get(self, index: int) -> QRegStorage:
        """
        Get the quantum register according to the index

        Create the register when it does not exists

        :param index: the quantum register index
        :return: QuantumRegisterStorage
        """

        value = self.registerMap.get(index)
        if value is None:
            value = QRegStorage(index, self.env)
            self.registerMap[index] = value
        return value

    def changeEnv(self, env: 'Scheduler') -> None:
        """
        Change the environment

        :param env: the environment to be changed to
        :return: None
        """
        self.env = env
        for qReg in self.registerMap.values():
            qReg.env = env
