class DList:
    def __init__(self):
        self.head = None
        self.end = None

    def add_to_front(self, val):
        new_node = DLNode(val)
        current_head = self.head
        new_node.next = current_head
        if current_head != None:
            current_head.prev = new_node
        else:
            self.end = new_node
        self.head = new_node
        return self

    def add_to_back(self, val):
        if self.head == None:	# si la lista está vacia
            self.add_to_front(val)	# ejecuta el método add_to_front
            return self	# asegurémonos de que el resto de esta función no suceda si agregamos al frente
        new_node = DLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        new_node.prev = runner
        self.end = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next

    def print_reverse_values(self):
        runner = self.end
        while (runner != None):
            print(runner.value)
            runner = runner.prev
        return self	

    def remove_val(self, val):
        runner = self.head
        if runner.value == val:
            self.head = runner.next
            self.head.prev = None
            return self
        while runner != None:
            runner = runner.next
            if runner.value == val:
                break
        if runner.value == val:
            runner.prev.next = runner.next
            runner.next.prev = runner.prev
        return self

    def insert_at(self, val, n):
        runner = self.head
        i = 0
        while (runner != None):
            i += 1
            runner = runner.next
        if i == 0:
            print('la lista esta vacia')
        if n == 0 or n > i:
            print('numero debe estar entre 1 y largo de la lista: ', i)
            return self
        
        new_node = DLNode(val)
        runner = self.head
        if n == 1:
            self.add_to_front(new_node)
            return self
        i = 1
        while runner != None:
            runner = runner.next
            i += 1
            if n == i:
                break
        if n == i:
            runner.prev.next = new_node
            new_node.next = runner
            new_node.prev = runner.prev
            runner.prev = new_node

        return self

class DLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

if __name__ == '__main__':
    my_list = DList()	# crear una nueva instancia de una lista
    my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_reverse_values()
    my_list.remove_val("are").print_reverse_values()
    my_list.insert_at("are",2).print_reverse_values().print_values()
 