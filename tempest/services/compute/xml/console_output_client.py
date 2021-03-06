# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2012 IBM
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


from lxml import etree
from tempest.common.rest_client import RestClientXML
from tempest.services.compute.xml.common import Document
from tempest.services.compute.xml.common import Element
from tempest.services.compute.xml.common import Text
from tempest.services.compute.xml.common import xml_to_json


class ConsoleOutputsClientXML(RestClientXML):

    def __init__(self, config, username, password, auth_url, tenant_name=None):
        super(ConsoleOutputsClientXML, self).__init__(config, username,
                                                      password,
                                                      auth_url, tenant_name)
        self.service = self.config.compute.catalog_type

    def get_console_output(self, server_id, length):
        post_body = Element("os-getConsoleOutput", length=length)
        resp, body = self.post("/servers/%s/action" % server_id,
                               headers=self.headers,
                               body=str(Document(post_body)))
        body = xml_to_json(etree.fromstring(body))
        return resp, body
