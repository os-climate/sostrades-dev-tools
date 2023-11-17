'''
Copyright 2023 Capgemini

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import os
from sos_trades_api.server import base_server
from sos_trades_api.server.base_server  import app, db
from sos_trades_api.models.database_models import User, UserProfile, Group, AccessRights, GroupAccessUser

with app.app_context():
    
    if len(User.query.all()) == 0:
    
        initial_account_name = os.environ.get('INITIAL_ACCOUNT_NAME')
        initial_account_password = os.environ.get('INITIAL_ACCOUNT_PASSWORD')
        if initial_account_name and initial_account_password:

            user_profile = UserProfile.query.filter(UserProfile.name == UserProfile.STUDY_MANAGER).first()
            all_user_group = Group.query.filter(Group.name == Group.ALL_USERS_GROUP).first()
            dev_user_group = Group.query.filter(Group.name == Group.SOS_TRADES_DEV_GROUP).first()
            member_right = AccessRights.query.filter(AccessRights.access_right == AccessRights.MANAGER).first()

            if user_profile is not None:
                user = User()
                user.username = initial_account_name
                user.firstname = initial_account_name
                user.firstname = initial_account_name
                user.lastname = initial_account_name
                user.account_source = User.LOCAL_ACCOUNT
                user.user_profile_id = user_profile.id
                user.set_password(initial_account_password)

                db.session.add(user)
                db.session.flush()
        
                user_access_group = GroupAccessUser()
                user_access_group.group_id = all_user_group.id
                user_access_group.user_id = user.id
                user_access_group.right_id = member_right.id

                db.session.add(user_access_group)

                user_dev_group = GroupAccessUser()
                user_dev_group.group_id = dev_user_group.id
                user_dev_group.user_id = user.id
                user_dev_group.right_id = member_right.id

                db.session.add(user_dev_group)
                db.session.commit()

