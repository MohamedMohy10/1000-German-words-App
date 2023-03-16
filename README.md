# 1000 German words App
Learn the most common used 1000 German words easily through flash cards

## How it works 
- The App at first picks a random German word from the main dataset 'data/german_words.csv' and views it

![image](https://user-images.githubusercontent.com/61654046/225767738-0b0b1690-98dd-4460-a085-e786bd69f8ae.png)


- After 5 seconds, the English translation is shown on screen


![image](https://user-images.githubusercontent.com/61654046/225767808-d740b56c-a149-4345-94a4-4fd197107638.png)


- If the user feel that he don't memorize it well and wants see this word again, then he clicks the red button ❌, 
  Otherwise, If he is confident that he knows this word very well and doesn't want the program to show it again then he should click the green button ✔

- The program saves the user's progress by creating a new file 'words_to_learn.csv' in the 'data' folder with all the words of the main dataset excluding the ones that the user confirmed that he don't need them to be shown again
- The program then picks another random word and shows it to the user, and so on ..
- The cycle continue until the user exits the program 
- The 'words_to_learn.csv' file will be the program's new data reference when the user opens the app again

- Your Goal is to memorize the 1000 word so the 'words_to_learn.csv' file becomes empty one day ..


#### The words dataset is taken from [strommeninc](https://strommeninc.com/1000-most-common-german-words-frequency-vocabulary/) website

