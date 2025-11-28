# ==========================
# QSPR_GEN Prediction Script
# ==========================

# Import required packages
import molvecgen
import pickle
# QSPR_GEN module import

# --------------------------
# Step 1: Initialize QSPR_GEN model
# --------------------------
model_path = "models/QSPR_GEN_model"  # Provide path to your trained QSPR_GEN model
qspr_engine = qgen.DDC(model_name=model_path)
print("Loaded QSPR_GEN model successfully.")

# --------------------------
# Step 2: Load trained QSAR/QSPR classifier (optional)
# --------------------------
classifier_path = "models/qsar_model.pickle"  # Path to saved classifier
with open(classifier_path, "rb") as f:
    qsar_classifier = pickle.load(f)["classifier_sv"]
print("QSAR/QSPR classifier loaded successfully.")

# --------------------------
# Step 3: Define a prediction function
# --------------------------
def predict_molecule_property(smiles_string):
    """
    Converts SMILES to latent vector and predicts property using QSAR/QSPR classifier.
    Returns the predicted value or an error message.
    """
    try:
        latent = qspr_engine.mol_to_latent(smiles_string)
        prediction = qsar_classifier.predict([latent])
        return prediction[0]
    except Exception as err:
        return f"Prediction failed: {err}"

# --------------------------
# Step 4: Run example prediction
# --------------------------
if __name__ == "__main__":
    example_smiles = "CCO"  # Replace with your SMILES input
    predicted_value = predict_molecule_property(example_smiles)
    print(f"Input SMILES: {example_smiles}")
    print(f"Predicted property: {predicted_value}")
