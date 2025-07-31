pipeline {
    agent any

    environment {
        CONDA_PATH = 'C:\\Users\\haito\\anaconda3\\Scripts\\activate.bat'  // or wherever your conda is installed
        ENV_NAME = 'machine_learning'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/haitomnsg/jenkinsDemo'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat """
                    call %CONDA_PATH% %ENV_NAME%
                    pytest
                """
            }
        }

        stage('Deploy') {
            steps {
                bat """
                    call %CONDA_PATH% %ENV_NAME%
                    taskkill /F /IM python.exe || echo "No running app"
                    start /B python app.py
                """
            }
        }
    }
}
