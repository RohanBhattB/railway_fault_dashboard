from model import train_and_predict

df = train_and_predict()

print(df[["Predicted_Label", "Condition"]].value_counts())
