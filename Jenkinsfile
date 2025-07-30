pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    pkill -f app.py || true
                    nohup ./venv/bin/python app.py > log.txt 2>&1 &
                '''
            }
        }
    }
}