# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "A record that meets the criteria of being a homeowner and having a low annual income qualifies for two distinct rules simultaneously, indicating that these rules are not mutually exclusive."
    answers["(b) explain"] = "The rules are not comprehensive because they do not cover cases where the Marital Status is Divorced."
    answers["(c) explain"] = "Due to the presence of overlapping rules, establishing a hierarchy is essential; generally, organizing rules systematically is considered best practice. For instance, a record characterized by both Home Ownership as No and Marital Status as Single will meet the criteria of two separate rules within the specified rule set."
    answers["(d) explain"] = "The necessity for a default class arises because a record with Marital Status = Divorced and Home Owner = No does not align with any of the specified rules.."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Based on the given rules and dataset, no vertebrate would be eligible to be classified as more than one class. Thus the rules are mutually exclusive."
    answers["(b) example"] = "Amphibians are not classified by any of these rules, thus these rules are not exhaustive"
    answers["(c) example"] = "There are no overlaps thus ordering not necessary"

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "Gradient of weights are calculated using chain-rule. Thus the (k+1)th gradient can be calculated using the kth weight's gradient in back propagation since it goes from op layer to ip layer"
    answers["(b) explain"] = "The activation in the node of k+1 layer is weighted sum of the kth layer, thus can be used for the calculation."
    answers["(c) explain"] = "The given fact is called overfitting and not vanishing gradient"
    answers["(d) explain"] = "The gradient of loss would be 0 if the input is 0 or the loss is converged to global minimum"

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.32

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "Choosing \(k=5\) offers a balanced approach, as \(k=1\) treats each data point as its own cluster, while \(k=50\) may obscure the data's local structure by overly generalizing cluster formation."
    answers["(b) explain"] = "It selects a sufficiently small number of neighbors to discern local patterns within the data without being so limited as to become excessively susceptible to noise."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "In cases where the class is \(+\) and \(A = 1\), there are 3 instances, and the total number of instances where the class is \(+\) is 5, thus yielding a fraction of \(3/5 = 0.6\)."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0  ## Verify

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "Using Naive Bayes, the probability for the \(+\) class is calculated as \(0.192\) (by multiplying the relevant values for instances where the class is \(+\)), and for the \(-\) class, it is \(0.032\). Therefore, the \(+\) class is predicted based on Naive Bayes."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'no'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "No since P(X|YZ)[0.5] != P(X|Z)[0.6], where X = (A=1), Y = (B=1) and Z = +"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
