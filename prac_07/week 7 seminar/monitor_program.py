from monitor import monitor

monitor1 = monitor("dell",1920,1080)
monitor2 = monitor("apple",1910,1000)

print(monitor1)
print(monitor2.get_resolution())
print(monitor1.get_total_pixels())
print(monitor1 == monitor2)
