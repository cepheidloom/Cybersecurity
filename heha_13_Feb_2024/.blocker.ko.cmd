savedcmd_/home/tron/heha/blocker.ko := ld -r -m elf_x86_64 -z noexecstack --build-id=sha1  -T scripts/module.lds -o /home/tron/heha/blocker.ko /home/tron/heha/blocker.o /home/tron/heha/blocker.mod.o;  make -f ./arch/x86/Makefile.postlink /home/tron/heha/blocker.ko