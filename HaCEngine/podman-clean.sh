#!/bin/bash
echo "Cleaning up all airflow dirs created by podman"
rm -rf config dags logs plugins 
