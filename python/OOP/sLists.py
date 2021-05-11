class SList:
    def __init__(self):
        self.head = None
        
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node    # Coloca la lista de la cabecera al nodo que se creó en el paso anterior
        return self             # return self para permitir las cadenas

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self	

    def add_to_back(self, val):
        if self.head == None:	# si la lista está vacia
            self.add_to_front(val)	# ejecuta el método add_to_front
            return self	# asegurémonos de que el resto de esta función no suceda si agregamos al frente
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	# Incrementa el corredor al siguiente nodo de la lista.
        return self

    def remove_from_front(self):
        runner = self.head
        self.head = self.head.next
        print('se elmino: ', runner.value)
        return self

    def remove_from_back(self):
        runner = self.head
        while (runner.next.next != None):
            runner = runner.next
        print ('se elimino ultimo valor: ', runner.next.value)
        runner.next = None
        return self

    def remove_val(self, val):
        runner = self.head
        before = runner
        if runner.value == val:
            self.head = runner.next
            return self
        while runner != None:
            before = runner
            runner = runner.next
            if runner.value == val:
                break
        if runner.value == val:
            before.next = runner.next
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
        
        new_node = SLNode(val)
        runner = self.head
        before = runner
        if n == 1:
            self.head = new_node
            self.head.next = runner
            return self
        i = 0
        while runner != None:
            before = runner
            runner = runner.next
            i += 1
            if n == i:
                break
        if n == i:
            before.next = new_node
            new_node.next = runner
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


if __name__ == '__main__':
    my_list = SList()	# crear una nueva instancia de una lista
    my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
    # my_list.remove_from_front().print_values()
    # my_list.remove_from_back().print_values()
    my_list.remove_val("fun!").print_values()
    my_list.insert_at("link",1).print_values()
    my_list.insert_at("last",5).print_values()