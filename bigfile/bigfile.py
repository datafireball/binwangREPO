from multiprocessing import Process, Queue
import time

# Customized this part to be yourprocess.
def myprocess(line):
    result = line + ' processed'
    time.sleep(2)
    return result

# Atomic function for each process
def f(filename, number, q, num):
    with open(filename) as file_in:
        for idx, line in enumerate(file_in):
            if idx % num == number:
                result = "{0}:{1}".format(str(number), myprocess(line.strip()))
                print result
                q.put(result)
                
def main():
    q = Queue()

    number_of_processes = 4
    plist = []
    
    for i in range(number_of_processes):
        plist.append(Process(target=f, args=('file_in.txt', i, q, number_of_processes)))

    for p in plist:
        p.start()
        
    for p in plist:
        p.join()
    
    q.put(None)
    
    print 'all joined!'
    # Loop through all the elements in the queue and write to file
    with open("file_out.txt", "w") as file_output:
        while True:
            item = q.get()
            print item

            if item is None:
                break
            print >>file_output, item
     
    print 'Done'
    
if __name__ == '__main__':
    main()
