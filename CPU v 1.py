# first attempt at making a cpu in python
# put the commands in the `instructions` list and run the program

'''
commands:

'0' : Get data from memory with the instruction after next as the address, load into a register with the next instruction as an ID

'1' : Add data from all registers and put in accumulator

'2' : output contents of accumulator to console

'3' : store contents of accumulator in memory

'4' : load contents of memory into a register with the ID of the next instruction and output it to the console

'''
instructions = ['0',0,0,'0',1,1,'1','2','4',0]
memory = [2,3]
accumulator = 0
for step in range(len(instructions)):
  if instructions[step] == '0':
    if instructions[step + 1] == 0:
        register0 = memory[instructions[step + 1]]
    elif instructions[step + 1] == 1:
        register1 = memory[instructions[step + 1]]
  elif instructions[step] == '1':
    accumulator = register0 + register1
  elif instructions[step] == '2':
    print(accumulator)
  elif instructions[step] == '3':
    memory.append(accumulator)
  elif instructions[step] == '4':
    for x in range(len(memory)):
      if instructions[step + 1] == 0:
        register0 = memory[x]
        print(register0)
      elif instructions[step + 1] == 1:
        register1 = memory[x]
        print(register1)
