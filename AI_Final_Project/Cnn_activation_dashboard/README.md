# CNN Activation Function Comparison Dashboard

This project is a Dash web application that allows users to compare different Tanh activation function variants on the CIFAR-10 dataset. Users can select an activation function from a dropdown menu to view its final validation accuracy and an interactive plot of validation accuracy over epochs.

## **Project Structure**

- `app.py`: The main Dash application script.
- `final_accuracies.csv`: CSV file containing the final validation accuracies for each activation function.
- `histories.json`: JSON file containing the training histories (accuracy and validation accuracy per epoch) for each activation function.
- `requirements.txt`: List of Python dependencies and their versions.
- `README.md`: This file.

## **Setup Instructions**

### **Prerequisites**

- Python 3.9 or compatible version installed on your system.
- `pip` package manager.

### **Steps**

1. **Clone or Download the Project**

   Clone this repository or download it as a ZIP file and extract it.

2. **Navigate to the Project Directory**

   ```bash
   cd cnn_activation_dashboard
