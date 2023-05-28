from user.User import User
from user.UserBuilder import UserBuilder

user=UserBuilder.item().withFirstName("Atif").withLastName("Hussain").withAge(23).liveInStreet("xyz").build()
user.print()