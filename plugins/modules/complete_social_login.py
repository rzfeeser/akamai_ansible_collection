#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: complete_social_login

short_description: covers api located at https://techdocs.akamai.com/identity-cloud-auth/reference/post-oauth-auth-native

version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    hostname:
        description: hostname of akamai api
        required: true
        type: str
    flow:
        description: Name of the flow configured for the desired login or registration experience.
        required: false
        type: str
        default: "standard"
    token:
        description: auth token of akamai api
        required: true
        type: str
    locale:
        description: Language code to use for the profile management experience. This member determines the language for any error messages returned to you and for any emails sent by Akamai to users.
        required: false
        type: str
        default: fr-CA

# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Complete social login
  rzfeeser.akamai.complete_social_login:
    hostname: 10.10.2.23   # required
    locale: fr-CA          # optional
    flow: standard         # optional
    token: "{{ token }}"   # required
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
http_response_code:
    description: the http response code that was returned
    type: int
    returned: always
    sample: 200
akamai_json:
    description: The json response sent back from the akamai api
    type: dict
    returned: always
    sample:
      "is_new": false
      "stat": "ok"
      "access_token": "z0y98xv76u5t4rs3"
'''

from ansible.module_utils.basic import AnsibleModule
import requests


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        hostname=dict(type='str', required=True),
        flow=dict(type='str', required=False, default="standard"),
        token=dict(type='str', required=True),
        locale=dict(type='str', required=False, default="fr-CA"),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        http_response_code=0,
        akamai_json={}
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    response = requests.get(module.params['hostname'])


    result['http_response_code'] = response.status_code
    result['akamai_json'] = response.json()

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
