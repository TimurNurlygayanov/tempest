# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools
from tempest import exceptions
from tempest.test import attr
from tempest.tests.murano import base
import time

class SanityMuranoTest(base.MuranoTest):

    @attr(type='positive')
    def test_create_and_deploying_ad(self):
        """ Create and deploy AD
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add AD
            4. Send request to deploy AD
            5. Send request to get info for check deloyment status
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        resp, sessinfo = self.get_session_info(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert (k > 7 and k <= 120)
        resp, envo = self.get_deployments_list(env['id'])
        assert envo['deployments'][0]['state'] == 'success'
        resp, infa = self.get_deployment_info(env['id'],
                                              envo['deployments'][0]['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='positive')
    def test_create_and_deploying_iis(self):
        """ Create and deploy IIS
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add IIS
            4. Send request to deploy IIS
            5. Send request to get info for check deloyment status
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_IIS(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        resp, sessinfo = self.get_session_info(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert (k > 7 and k <= 120)
        resp, envo = self.get_deployments_list(env['id'])
        assert envo['deployments'][0]['state'] == 'success'
        resp, infa = self.get_deployment_info(env['id'],
                                              envo['deployments'][0]['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='positive')
    def test_create_and_deploying_apsnet(self):
        """ Create and deploy apsnet
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add apsnet
            4. Send request to deploy apsnet
            5. Send request to get info for check deloyment status
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_apsnet(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        resp, sessinfo = self.get_session_info(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert (k > 7 and k <= 120)
        resp, envo = self.get_deployments_list(env['id'])
        assert envo['deployments'][0]['state'] == 'success'
        resp, infa = self.get_deployment_info(env['id'],
                                              envo['deployments'][0]['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='positive')
    def test_create_and_deploying_iis_farm(self):
        """ Create and deploy IIS farm
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add IIS farm
            4. Send request to deploy IIS farm
            5. Send request to get info for check deloyment status
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_IIS_farm(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        resp, sessinfo = self.get_session_info(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert (k > 7 and k <= 120)
        resp, envo = self.get_deployments_list(env['id'])
        assert envo['deployments'][0]['state'] == 'success'
        resp, infa = self.get_deployment_info(env['id'],
                                              envo['deployments'][0]['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='positive')
    def test_create_and_deploying_apsnet_farm(self):
        """ Create and deploy apsnet farm
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add apsnet farm
            4. Send request to deploy apsnet farm
            5. Send request to get info for check deloyment status
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_apsnet_farm(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        resp, sessinfo = self.get_session_info(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert (k > 7 and k <= 120)
        resp, envo = self.get_deployments_list(env['id'])
        assert envo['deployments'][0]['state'] == 'success'
        resp, infa = self.get_deployment_info(env['id'],
                                              envo['deployments'][0]['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='positive')
    def test_create_and_deploying_sql(self):
        """ Create and deploy SQL
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add SQL
            4. Send request to deploy SQL
            5. Send request to get info for check deloyment status
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_SQL(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        resp, sessinfo = self.get_session_info(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert (k > 7 and k <= 120)
        resp, envo = self.get_deployments_list(env['id'])
        assert envo['deployments'][0]['state'] == 'success'
        resp, infa = self.get_deployment_info(env['id'],
                                              envo['deployments'][0]['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='positive')
    def test_create_and_deploying_sql_cluster(self):
        """ Create and deploy SQL cluster
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add AD
            4. Send request to deploy AD
            5. Send request to create new session
            6. Send request to add SQL cluster
            7. Send request to deploy SQL cluster
            8. Send request to get info for check deloyment status
            9. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        resp, sessinfo = self.get_session_info(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert (k > 7 and k <= 120)
        resp, envo = self.get_deployments_list(env['id'])
        assert envo['deployments'][0]['state'] == 'success'
        resp, sess = self.create_session(env['id'])
        resp, serv1 = self.create_SQL_cluster(env['id'], sess['id'],
                                              serv['domain'])
        resp = self.deploy_session(env['id'], sess['id'])
        resp, sessinfo = self.get_session_info(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert (k > 7 and k <= 120)
        resp, envo = self.get_deployments_list(env['id'])
        #for i in envo['deployments']:
            #assert i['state'] == 'success'
        #assert envo['deployments'][0]['state'] == 'success'
        resp, infa = self.get_deployment_info(env['id'],
                                              envo['deployments'][0]['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_get_deployments_list_wo_env_id(self):
        """ Try to get deployments list without env id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to get deployments list using uncorrect
               environment id
            4. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        self.assertRaises(Exception, self.get_deployments_list, None)
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_create_service_after_begin_of_deploy(self):
        """ Try to create service after begin of deploy
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to create AD
            4. Send request to deploy session
            5. Send request to create IIS
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        self.assertRaises(Exception, self.create_IIS,
                          env['id'], sess['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_delete_service_after_begin_of_deploy(self):
        """ Try to delete service after begin of deploy
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to create AD
            4. Send request to deploy session
            5. Send request to delete AD
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        self.assertRaises(Exception, self.delete_service, env['id'],
                          sess['id'], serv['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_deploy_after_delete_environment(self):
        """ Try to deploy session after deleting environment
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to create AD
            4. Send request to delete environment
            5. Send request to deploy session
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        resp = self.delete_environment(env['id'])
        self.assertRaises(Exception, self.deploy_session, env['id'],
                          sess['id'])

    @attr(type='negative')
    def test_deploy_after_delete_session(self):
        """ Try to deploy session after deleting this session
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to create AD
            4. Send request to delete session
            5. Send request to deploy session
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        resp = self.delete_session(env['id'], sess['id'])
        self.assertRaises(Exception, self.deploy_session, env['id'], "")
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_deploy_empty_environment(self):
        """ Deploy empty environment
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to deploy session
            4. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        env.update({'status': None})
        k = 0
        while env['status'] != "ready":
            time.sleep(15)
            k += 1
            resp, env = self.get_environment_by_id(env['id'])
            if not env.has_key('status'):
                env.update({'status': None})
            if k > 120:
                break
        assert k < 8
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_deploy_second_session_after_first(self):
        """ Try to deploy second session after begin of deploy first session
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session1
            3. Send request to create session2
            4. Send request to deploy session1
            5. Send request to deploy session2
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess1 = self.create_session(env['id'])
        resp, sess2 = self.create_session(env['id'])
        resp = self.deploy_session(env['id'], sess1['id'])
        self.assertRaises(Exception, self.deploy_session, env['id'],
                          sess2['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_deploy_second_session_after_first_with_add_service(self):
        """ Try to deploy session after deleting this session
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session1
            3. Send request to create session2
            4. Send request to deploy session1
            5. Send request to create AD
            6. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess1 = self.create_session(env['id'])
        resp, sess2 = self.create_session(env['id'])
        resp = self.deploy_session(env['id'], sess1['id'])
        self.assertRaises(Exception, self.create_AD, env['id'], sess2['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_deploy_session_wo_env_id(self):
        """ Try to deploy session without environment id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to create AD
            4. Send request to deploy session using wrong environment id
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        self.assertRaises(Exception, self.deploy_session, None,
                          sess['id'])
        resp = self.delete_environment(env['id'])

    @attr(type='negative')
    def test_get_deployment_info_wo_env_id(self):
        """ Try to get deployment info without environment id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to create AD
            4. Send request to deploy session
            5. Send request to get deployments list
            6. Send request to get deployment info using wrong environment id
            7. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        resp = self.deploy_session(env['id'], sess['id'])
        time.sleep(5)
        resp, envo = self.get_deployments_list(env['id'])
        self.assertRaises(Exception, self.get_deployment_info,
                          None, envo['deployments'][0]['id'])
        resp = self.delete_environment(env['id'])
