pipeline {
    agent any

    environment {
        PROJECT_NAME = 'calculator-ci'
        PYTHON = 'python'
    }

    stages {

        stage('Clone / Pull Repository') {
            steps {
                echo 'Cloning repository from GitHub...'
                checkout scm
                echo 'Repository cloned successfully.'
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                bat '''
                    %PYTHON% -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install pytest pytest-html
                '''
                echo 'Python environment ready.'
            }
        }

        stage('Build / Lint') {
            steps {
                echo 'Checking Python syntax...'
                bat '''
                    call venv\\Scripts\\activate.bat
                    %PYTHON% -m py_compile calculator/calculator.py
                    echo Syntax OK: calculator.py
                '''
                echo 'Build/lint stage passed.'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests with pytest...'
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest tests/ --tb=short -v
                '''
                echo 'All tests passed.'
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully! All stages passed.'
        }
        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }
        always {
            echo 'Cleaning up...'
            bat 'if exist venv rmdir /s /q venv'
        }
    }
}
