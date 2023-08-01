import instaloader

def getBasic_profile_details():
    profile_Id = input("Enter the Instagram User_Id: ")
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, profile_Id)

    print("User_Name:", profile.username)
    print("User_Id:", profile.userid)
    print("Number_Total_No_of_posts:", profile.mediacount)
    print("My_total_followers_people_counts_are:", profile.followers)
    print("This_peoples_are_following_my_profile:", profile.followees)
    print("bio:", profile.biography)
    print("External_URL:", profile.external_url)
    print('\n')

def download_latest_five_posts_on_Instragram():
    user_Id = input("Enter your Instagram User_Id: ")

    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, user_Id)

    # Download the profile picture
    L.download_profile(user_Id, profile_pic_only=True)

    # Retrieve the latest five posts and download them
    posts = profile.get_posts()
    count = 0
    for index, post in enumerate(posts, 1):
        if count < 5:
            L.download_post(post, target=f"{profile.username}_{index}")
            count += 1
        else:
            break

if __name__ == '__main__':
    option = '0'
    while option != '3':
        option = input("Choose an Option Number:\n1) Get Basic details of any Instagram account\n2) Download Latest Five posts and profile photo of any Instagram user\n3) Exit This Application\n")

        if option == '1':
            getBasic_profile_details()
        elif option == '2':
            download_latest_five_posts_on_Instragram()
        elif option == '3':
            exit()
        else:
            print("Wrong input. Please try again.")
