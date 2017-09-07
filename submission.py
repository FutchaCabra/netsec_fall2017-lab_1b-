from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING, BUFFER, BOOL, ListFieldType
class Access(PacketType):
	def Access(): 
		DEFINITION_IDENTIFIER = "network.access"
		DEFINITION_VERSION = "2.0"
	
		FIELDS = [
			("name", STRING),
			("data", BUFFER)
			]
	
		packet1 = Access()
		packet1.name = "RequestUserName"
		packet1.data = "What is your name?"
		
		
	
class Username(PacketType): 
	def Username():
		DEFINITION_IDENTIFIER = "network.Username"
		DEFINITION_VERSION = "2.0"
	
		FIELDS = [
			("title", STRING),
			("data", BUFFER)
			]	
	
		packet2 = Access()
		packet2.title = "UserName"
		packet2.data = "Sean Futch"
		
		
	
class PasswordRequest(PacketType): 
	def PasswordRequest():
		DEFINITION_IDENTIFIER = "network.PasswordRequest"
		DEFINITION_VERSION = "2.0"
	
		FIELDS = [
			("Request", STRING),
			("data", BUFFER)
			]	
	
		packet3 = Password()
		packet3.Request = "Password Request"
		packet3.data = "Please Enter Password."
		
		
	
class UserPassword(PacketType):
	def UserPassword(): 
		DEFINITION_IDENTIFIER = "network.UserPassword"
		DEFINITION_VERSION = "2.0"
	
		FIELDS = [
			("data", BUFFER)
			]	
	
		packet4 = UserPassword()
		packet4.data = "Password"
	
	# deserializer = Access.Deserializer()
	
	def basicUnitTest():
		packet1 = Access()
		packet1Bytes = packet1.__serialize__()
		print (packet1)
		packet1a = Access.Deserialize(packet1Bytes)
		print (packet1a)
		assert packet1 == packet1a
		
		packet2 = Username()
		packet2Bytes = packet2.__serialize__()
		packet2a = Username.Deserialize(packet2Bytes)
		assert packet2 == packet2a
		
		packet3 = PasswordRequest()
		packet3Bytes = packet3.__serialize__()
		packet3a = PasswordRequest.Deserialize(packet3Bytes)
		assert packet3 == packet3a
		
		packet4 = UserPassword()
		packet4Bytes = packet4.__serialize__()
		packet4a = UserPassword.Deserialize(packet4Bytes)
		assert packet4 == packet4a
		
	if __name__=="__main__":
		basicUnitTest()
		
		
	print ("Basic Unit Test Completed")
		
	
	#for packet in deserializer.nextPackets():
	#	print ("got a packet")
	#	if packet == packet1: print ("It's packet 1!") 
	#	elif packet == packet2: print ("It's packet 2!") 
	#	elif packet == packet3: print ("It's packet 3!")
	#	elif packet == packet4: print ("It's packet 4!")
