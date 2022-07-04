pipeline {
    agent {
        docker { image 'python:3.8-alpine3.15' }
    }
    environment {
        dockerhub = credentials('dockerhub_luna4444')
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
        stage('Merge into Main')
        {
            steps {
                sh 'git checkout main'
                sh 'git merge dev'
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
