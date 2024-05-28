class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            print("The queue is empty, no one to serve.")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def display(self):
        if self.is_empty():
            print("The queue is empty.")
            return
        current = self.front
        print("Current queue:")
        while current:
            print(f"Name: {current.data['name']}, Order: {current.data['order']}")
            current = current.next

def coffee_shop_queue():
    queue = Queue()
    
    while True:
        queue.display()
        print("\nChoose an action:")
        print("1. Serve the first person")
        print("2. Add a person to the queue")
        #print("3. Display the queue")
        print("4. Quit")
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == '4' or choice == 'quit':
            print("Thanks for using the coffee shop queue system!")
            break
        elif choice == '1':
            served_person = queue.dequeue()
            if served_person:
                print(f"Served: {served_person['name']}, Order: {served_person['order']}")
        elif choice == '2':
            name = input("Enter the person's name: ").strip()
            order = input("Enter the person's order: ").strip()
            queue.enqueue({'name': name, 'order': order})
            print(f"Added {name} with order {order} to the queue.")
        elif choice == '3':
            queue.display()
        else:
            print("Invalid choice. Please try again.")

# Run the coffee shop queue system
coffee_shop_queue()
