savedcmd_/home/tron/heha/blocker.mod := printf '%s\n'   blocker.o | awk '!x[$$0]++ { print("/home/tron/heha/"$$0) }' > /home/tron/heha/blocker.mod
