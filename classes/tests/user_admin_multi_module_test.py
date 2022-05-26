from single_admin_module import Admin

master_lu_privileges = ['antivirus','check computer health']
master_lu = Admin('lu','dashi','male',master_lu_privileges)
master_lu.describe_user()
master_lu.show_privileges()
