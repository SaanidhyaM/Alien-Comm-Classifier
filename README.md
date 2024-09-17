# Alien-Comm-Classifier
Upon landing on the planet Xernia, your crew intercepts a flood of mysterious
transmissions from various alien species. To achieve your mission objectives,
you must analyze and decode these messages to identify which species sent each
one.

You are provided with a dataset (data.csv) containing intercepted alien
messages, where each message is associated with specific attributes such as the
alien species, number of fingers, and whether they possess a tail. Your task is
to classify these transmissions based on these attributes.

Dataset (Alien Messages Corpus)
The intercepted transmissions are structured as follows:

• Message: The alien communication in text form.

• Species: The species that sent the message.

• Number of Fingers: The typical number of fingers for the species.

• Tail: A yes/no field indicating whether the species has a tail.

Task
You talked to a lot of aliens this time and want to test how accurate your
prediction skill has become. You thus log all your conversations, observe the
number of fingers and the existence of tails for these new aliens in test.csv.
Your goal is to identify the species of aliens in test.csv based on the intercepted
messages, number of fingers, and presence of a tail. Submit a result.csv file
only containing a column titled ’Species’ that contains species for each row of
test.csv based on your predictions. This part will be graded on the accuracy
of the predictions in the result.csv file and the approach and cleanliness of
your solution (solution.ipynb). Ensure that your approach is clearly written
with comments and markdown cells in the python notebook that you submit.
