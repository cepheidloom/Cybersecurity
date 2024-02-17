To run this code, which is a Linux kernel module, you need to compile it and then load it into the kernel. Here are the steps:

1. Copy the file `blocker.c` in whichever directory you want.
    
2. You need a Makefile to compile the module. Create a file named `Makefile` in the same directory with the following content:
    
```Makefile
obj-m += blocker.o

all:

    make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:

    make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```
*Remember that the Makefile file will have no extension and you simply have to create a file named just "Makefile" using the touch command in linux.*

3. Now, compile the module by running `make` in the terminal:
```
make
```
5. If the module compiled successfully, you should see a `blocker.ko` file in the directory. This is the compiled module.
6. Now, load the module into the kernel:
```
sudo insmod blocker.ko
```
6. You can check if the module is loaded by:
```
lsmod | grep firewall
```
8. To remove the module, you can use:
```
sudo rmmod firewall
```

---
Once the kernel module (`.ko` file) is loaded into the kernel using `insmod`, it starts working immediately. Kernel modules are not like typical executables that you run from the command line. Instead, they extend the functionality of the kernel itself.

In this case, the module is designed to block DNS packets at port 53 coming from IP address 2.2.2.2. So, to test if it's working, you would need to generate such network traffic and see if it's being blocked.

You can use tools like `dig`, `nslookup`, or `netcat` to generate DNS requests.
After generating the traffic, you can check the kernel log messages using `dmesg` to see if your module is printing the "Packet Dropped" message. This would indicate that it's working as expected.

Remember to unload the module using `rmmod` when you're done testing.
