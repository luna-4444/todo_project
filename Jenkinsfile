pipeline {
    agent {
        docker { image 'python:3.8.10' }
    }
    environment {
        dockerhub = credentials('dockerhub_luna4444')
    }

    stages {
        stage('Build') {
            steps {
                // sh 'whoami'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 manage.py test'
            }
        }
        stage('Merge into Main')
        {
            steps {
                sh 'git config --global user.email "chandra.kiran@couture.ai"'
                sh 'git config --global user.name "luna-4444"'
                sh 'echo GitHub config successful!'
                sh 'git checkout main'
                sh 'git merge origin/dev'
            }
        }
        stage('Done') {
            steps {
                // sh 'git checkout dev'
                // sh 'git branch -D dev'
                sh 'Done mergning into main'
            }
        }
        // stage('Build Image') {
        //     steps {
        //         sh 'docker build -t todo_app_jenkins .'
        //     }
        // }
        // stage('Start Pushing to Docker Hub') {
        //         steps {
        //         sh 'docker tag todo_app_jenkins $dockerhub_USR/sample_repo:todo_app_jenkins'
        //         sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'

    //         sh 'docker push $dockerhub_USR/sample_repo:todo_app_jenkins'
    //         }
    // }
    }
}
