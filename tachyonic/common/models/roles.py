from __future__ import absolute_import
from __future__ import unicode_literals

from tachyonic.neutrino.model import Model
from tachyonic.neutrino.model import ModelDict


class RoleFields(object):
    class Meta(object):
        db_table = 'role'

    id = Model.Uuid(hidden=True)
    name = Model.Text(length=15,
                          max_length=15,
                          label="Role",
                          required=True)
    description = Model.Text(length=30,
                                 max_length=30,
                                 label="Description",
                                 required=False)
    creation_time = Model.Datetime(label="Created",
                                       placeholder="0000-00-00 00:00:00",
                                       readonly=True,
                                       length=20)


class Roles(RoleFields, Model):
    pass


class Role(RoleFields, ModelDict):
    pass
