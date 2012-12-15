# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack, LLC
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import nose
import unittest2 as unittest

from tempest import exceptions
from tempest import openstack
from tempest.common.utils.data_utils import rand_name


class BaseNetworkTest(unittest.TestCase):

    networks = None
    client = None

    @classmethod
    def setUpClass(cls):
        os = openstack.Manager()
        cls.client = os.network_client
        config = os.config
        cls.networks = []
        enabled = True

        # Validate that there is even an endpoint configured
        # for networks, and mark the attr for skipping if not
        try:
            cls.client.list_networks()
        except exceptions.EndpointNotFound:
            enabled = False
            skip_msg = "No OpenStack Network API endpoint"
            raise nose.SkipTest(skip_msg)

    @classmethod
    def tearDownClass(cls):
        for network in cls.networks:
            cls.client.delete_network(network['id'])


