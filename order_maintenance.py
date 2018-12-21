import sys


class full_persistant_node:
    def __init__(self, node_version, child_list, parent_pointer, node_value):
        self.node_version = node_version
        self.child_list = child_list
        self.parent_pointer = parent_pointer
        self.node_value = node_value


class apply_full_persistant:
    def __init__(self):
        self.storage = []
        self.node_counter = 1
        self.default()

    def default(self):
        temp_obj = full_persistant_node(1, [], None, input('Enter Value of Root : '))
        self.storage.append(temp_obj)
        self.node_counter += 1

    def create_node(self):
        print('----- For Create New Node -----')
        value = input('Enter Node Value to Store : ')
        print()

        temp_obj = full_persistant_node(self.node_counter, [], 1, value)

        for i in self.storage:
            if i.node_version == 1:
                i.child_list.append(self.node_counter)

        self.storage.append(temp_obj)

        print('New Node Version {} Created Successfully...'.format(self.node_counter))
        print()

        self.node_counter += 1

        return

    def update_node(self):
        flag = False

        print('----- For Update Node Version -----')
        version = int(input('Enter Version no. to be Update : '))
        value = input('Enter Node Value to Store : ')
        print()

        for i in self.storage:
            if version is i.node_version:
                flag = True

        if flag:
            temp_obj = full_persistant_node(self.node_counter, [], version, value)

            for i in self.storage:
                if version is i.node_version:
                    i.child_list.append(self.node_counter)

            self.storage.append(temp_obj)

            print('Node Version {} Successfully Updated With Creation of New Node Version {}...'
                  .format(version, self.node_counter))
            print()

            self.node_counter += 1

        else:
            print('Node Version {} is not present in DS...'.format(version))

        return

    def check_ancestor_input(self):
        flag = False

        print('----- For Checking Ancestor -----')
        temp_version = version_1 = int(input('Enter the Version no. For which Ancestor Check is to be done : '))
        version_2 = int(input('Enter the Version no. for Checking Ancestor or Not : '))
        print()

        for i in self.storage:
            if version_1 is i.node_version:
                flag = True

        if flag:
            while True:
                for node in self.storage:
                    if temp_version is node.node_version:
                        temp_version = node.parent_pointer

                        if version_2 is temp_version:
                            print('Node Version {} is Ancestor of Node Version {}...'.format(version_2, version_1))
                            print()
                            return
                        elif version_1 is None:
                            print('Node Version {} is not an Ancestor of Node Version {}...'
                                  .format(version_2, version_1))
                            print()
                            return
        else:
            print('Node Version {} is not present in DS...'.format(version_1))

        return

    def return_latest_version(self):
        flag = False

        print('----- For Finding Latest Node Version -----')
        version = int(input('Enter Version no. : '))
        print()

        for i in self.storage:
            if version is i.node_version:
                flag = True

        if flag:
            for i in self.storage:
                if version is i.node_version:

                    if not i.child_list:
                        print('The Node Version {} does not have any further updates...'.format(version))
                        return
                    else:
                        max_version = max(i.child_list)
                        print('The Node Version {} has Latest Updated Version {}...'.format(version, max_version))
                        print()

                        for node in self.storage:
                            if max_version is node.node_version:
                                print('Node Version : ', node.node_version)

                                print('Parent : ', node.parent_pointer)

                                if not node.child_list:
                                    print('No Child')
                                else:
                                    print('Child List : ', node.child_list)

                                print('Node Value : ', node.node_value)
                                print()
        else:
            print('Node Version {} is not present in DS...'.format(version))

        return

    def search_version(self):
        flag = False

        print('----- For Searching Node Version in DS -----')
        version = int(input('Enter Version no. : '))
        print()

        for i in self.storage:
            if version is i.node_version:
                flag = True

        if flag:
            for i in self.storage:
                if version is i.node_version:
                    print('Node Version : ', i.node_version)

                    print('Parent : ', i.parent_pointer)

                    if not i.child_list:
                        print('No Child')
                    else:
                        print('Child List : ', i.child_list)

                    print('Node Value : ', i.node_value)
                    print()

                    return
        else:
            print('Node Version {} is not present in DS...'.format(version))

        return

    def display_nodes(self):
        for i in self.storage:
            print('Node Version : ', i.node_version)

            print('Parent : ', i.parent_pointer)

            if not i.child_list:
                print('No Child')
            else:
                print('Child List : ', i.child_list)

            print('Node Value : ', i.node_value)
            print()

        return


if __name__ == '__main__':
    afp = apply_full_persistant()

    while True:
        print('--------------------------------------------------')
        print()
        ch = int(input('\n 1 --> Create New Version \n 2 --> Update Version \n 3 --> Check Ancestor '
                       '\n 4 --> Return Latest Version \n 5 --> Search Version \n 6 --> Display All Versions '
                       '\n Enter your choice : '))
        print()

        if ch is 1:
            afp.create_node()
        elif ch is 2:
            afp.update_node()
        elif ch is 3:
            afp.check_ancestor_input()
        elif ch is 4:
            afp.return_latest_version()
        elif ch is 5:
            afp.search_version()
        elif ch is 6:
            afp.display_nodes()
        else:
            sys.exit()
