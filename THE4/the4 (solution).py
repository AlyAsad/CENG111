# Aly Asad Gilani
# e2547875

def inheritance(Descriptions):

	children = {}
	parents = {}
	spouse = {}
	dead = []

	def alive_descendant(guy):
		alive= 0
		if guy not in children:
			return alive
		else:
			for i in range(0, len(children[guy])):
				if children[guy][i] not in dead:
					alive += 1
				else:
					alive += alive_descendant(children[guy][i])
		return alive > 0
        
	
	def child_sort(L):
		if L[1] in children:
			for i in range(3,len(L)):
				children[L[1]].append(L[i])
		elif L[1] not in children:
			children[L[1]]=L[3:]
		if L[2] in children:
			for i in range(3,len(L)):
				children[L[2]].append(L[i])
		elif L[2] not in children:
			children[L[2]]=L[3:]
		
		return
		
	def parent_sort(L):
		for i in range(3,len(L)):
			parents[L[i]]=L[1:3]
	
		return
		
	def spouse_sort(L):
		spouse[L[1]]=L[2]
		spouse[L[2]]=L[1]
		
		return
	
	length = len(Descriptions)
	
	for i in range(0,length):
		
		L = Descriptions[i].split(" ")
		
		if "CHILD" in L[0]:
			child_sort(L)
			parent_sort(L)
		elif "MARRIED" in L[0]:
			spouse_sort(L)
		elif "DEPARTED" in L[0]:
			dead.append(L[1])
		elif "DECEASED" in L[0]:
			dead.append(L[1])
			deceased= L[1]
			share= float(L[2])

	def PG11(deceased,share):
                shares = []
                total_heirs = 0
                for i in range(0, len(children[deceased])):
                        if children[deceased][i] not in dead or alive_descendant(children[deceased][i]):
                                total_heirs += 1
                for i in range(0, len(children[deceased])):
                        if children[deceased][i] not in dead:
                                shares.append((children[deceased][i], share / total_heirs))
                        elif alive_descendant(children[deceased][i]):
                                shares.extend(PG11(children[deceased][i], share / total_heirs))

                return shares

			
	def PG1(deceased,share):
		if alive_descendant(deceased) == False:
			return []
		else:
			shares=[]
			total_heirs=0
			if deceased in spouse and spouse[deceased] not in dead:
				shares.append((spouse[deceased],share*0.25))
				share= 0.75*share
			for i in range(0,len(children[deceased])):
				if children[deceased][i] not in dead or alive_descendant(children[deceased][i]):
					total_heirs += 1
			for i in range(0,len(children[deceased])):
				if children[deceased][i] not in dead:
					shares.append((children[deceased][i],share/total_heirs))
				elif alive_descendant(children[deceased][i]):
					shares.extend(PG11(children[deceased][i],share/total_heirs))


		return shares


	def PG2(deceased,share):
		if deceased not in parents: return []

		if (parents[deceased][0] in dead and alive_descendant(parents[deceased][0])== False) and (parents[deceased][1] in dead and alive_descendant(parents[deceased][1])== False):
			return []
		else:
			shares = []
			total_heirs=0
			if deceased in spouse and spouse[deceased] not in dead:
				shares.append((spouse[deceased],share*0.5))
				share=0.5*share
			if parents[deceased][0] not in dead or alive_descendant(parents[deceased][0]):
					total_heirs += 1
			if parents[deceased][1] not in dead or alive_descendant(parents[deceased][1]):
				total_heirs += 1
			if parents[deceased][0] not in dead:
				shares.append((parents[deceased][0],share/total_heirs))
			if parents[deceased][1] not in dead:
				shares.append((parents[deceased][1],share/total_heirs))
			if parents[deceased][0] in dead and alive_descendant(parents[deceased][0]):
				shares.extend(PG11(parents[deceased][0],share/total_heirs))
			if parents[deceased][1] in dead and alive_descendant(parents[deceased][1]):
				shares.extend(PG11(parents[deceased][1],share/total_heirs))

		return shares

	def PG3(deceased, share):
		if deceased not in parents: return []
		total=0
		shares = []
		grand=[]
		if parents[deceased][0] in parents:
			grand.append(parents[parents[deceased][0]][0])
			grand.append(parents[parents[deceased][0]][1])
		if parents[deceased][1] in parents:
			grand.append(parents[parents[deceased][1]][0])
			grand.append(parents[parents[deceased][1]][1])
			
		if grand==[]: return []
		for i in range(0,len(grand)):
			if grand[i] not in dead or alive_descendant(grand[i]):
				total += 1
		if total == 0: return []
		
		if deceased in spouse and spouse[deceased] not in dead:
			shares.append((spouse[deceased], 0.75*share))
			share = 0.25*share
			
			
		for i in range(0,len(grand)):
			if grand[i] not in dead:
				shares.append((grand[i],share/total))
			else:
				shares.extend(PG11(grand[i],share/total))

		return shares


	result = PG1(deceased,share)

	if result == []:
		result = PG2(deceased,share)
	if result == []:
                result = PG3(deceased,share)
	if result == [] and deceased in spouse and spouse[deceased] not in dead:
                result = [(spouse[deceased],share)]

                
	Changed = True
        
	while Changed:
		Changed = False
		for i in range(0,len(result)-1):
			for j in range(i+1, len(result)):
                                
				if j >= len(result): break
				
				if result[i][0] == result[j][0]:
                                        temp1 = result.pop(i)
                                        temp2 = result.pop(j-1)
                                        final = (temp1[0], temp1[1]+temp2[1])
                                        result.append(final)
                                        Changed = True
                                        

	
	return result


	
	
	
	
	
	
	
