from time import sleep, time
import threading

def write_words(words_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, words_count+1):
            file.write(f"Какое-то слово №{i}\n")
            sleep(0.1)
    print(f'Завершилась запись файла {file_name}')

start_time = time()


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f'Время {end_time - start_time}')

threads = []
file_name = ['example5.txt', 'example6.txt', 'example7.txt', 'example8.txt']
words_count = [10,30,200,100]

start_time = time()

for words_count, file_name in zip(words_count, file_name):
    thread = threading.Thread(target = write_words, args = (words_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time()

print(f'Время {end_time - start_time}')




