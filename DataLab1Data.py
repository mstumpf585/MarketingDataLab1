import pandas as pd 

# Question 1 ######################################
# Get Population dist of Geneder 
# read in data with pandas 
data = pd.read_csv("AFC.csv")

# write out report to MD file 
filename = "DataLabQuestions.md"
f = open(filename, "a")
f.truncate(0)

# write header 
f.write("# Question 1 Population Distribution \n")
# Get Population dist of everything 
for column in data: 

    if (column != 'id') and (column != 'revenue') and (column != 'age'): 
        print(column)
        f.write("### " + column + "\n")
        
        print(data[column].value_counts(normalize=True)*100)

        series = data[column].value_counts(normalize=True)*100
        seriesList = series.index.tolist()
        listIndex = 0
        for entry in series:
            f.write(str(seriesList[listIndex]) + " : " + str(entry) + "\n\n")
            listIndex+=1
        print("\n")
        f.write("\n")

f.write("## Bar Charts can be found in DataLabDeliverables\n")

# Question 2 ########################################
f.write("# Question 2 \n")
f.write("## Age Stats \n")
f.write("Average age :" + str(data["age"].mean()) + "\n\n")
f.write("Median age: " + str(data["age"].median()) + "\n\n") 
f.write("Std Dev age: " + str(data["age"].std()) + "\n\n") 
f.write("## thoughts on std dev \n")


# Question 3 ########################################
f.write("# Question 3\n")
f.write("Not really sure how to make this histogram do you want it all in one file? You can find them in DataLabDeliverables"
+ "I made two one with just age count and then with all 3 in the histogram \n")


# Question 4 ########################################
usedWeight = (data["weight"] == 1).sum()
usedClasses = (data["classes"] == 1).sum()
usedCircuit = (data["circuit"] == 1).sum()
usedStation = (data["station"] == 1).sum()
usedPool = (data["pool"] == 1).sum()

f.write("# Question 4\n")
f.write("## Service variables\n")
f.write("Used weight = " + str(usedWeight) + "\n\n")
f.write("Used classes = " + str(usedClasses) + "\n\n")
f.write("Used circuit = " + str(usedCircuit) + "\n\n")
f.write("Used station = " + str(usedStation) + "\n\n")
f.write("Used pool = " + str(usedPool) + "\n\n")

infoDoc = (data["doctor"] == 1).sum()
infoFriend = (data["wom"] == 1).sum()
infoAd = (data["advert"] == 1).sum()
infoSpeaker = (data["speaker"] == 1).sum()

f.write("## Info source variables \n")
f.write("Doctor recommendation " + str(infoDoc) + "\n\n")
f.write("Friend recommendation " + str(infoFriend) + "\n\n")
f.write("Advertisement " + str(infoAd) + "\n\n")
f.write("Speaker " + str(infoSpeaker) + "\n\n")

# Question 5 ############################################
f.write("## Number of Visits and Likely to Recommend\n\n")
f.write("### Visits\n\n")
f.write("Average Number of Visits " + str(data["visits"].mean()) + "\n\n")
f.write("Standard Error for Visits " + str(data["visits"].std()) + "\n\n")
f.write("### Likely to recommend \n\n")
f.write("Average Number of Likely to recommend " + str(data["recom"].mean()) + "\n\n")
f.write("Standard Error for Likely to recommend " + str(data["recom"].std()) + "\n\n")

# Question 6 ############################################
from scipy.stats import ttest_1samp
import numpy as np 

visits = data["visits"]
visitsMean = visits.mean()
tset, pval = ttest_1samp(visits.to_numpy(), 20, nan_policy='omit')

f.write("P-value for t test \n\n" + str(pval))
lowerThanPoint5 = pval < .05
f.write("P-value < .05 \n\n" + str(lowerThanPoint5))
f.write("### Thoughts on Hypothesis test: \n\n")

# Question 7 #########################################

