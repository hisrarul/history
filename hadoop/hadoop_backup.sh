#!/bin/bash
backup_date=$(date +%d-%m-%Y)
s3_path=s3_bucket_name
truncate -s 0 hadoop_paths_to_be_backup.txt

for path in $(cat hadoop_backup_paths.txt)
do
hdfs dfs -ls hdfs://$path | awk '{print $8}' >> hadoop_paths_to_be_backup.txt
done

for path in $(cat hadoop_paths_to_be_backup.txt)
do
    echo -e "############\nBackup started: $(date)\nPath: ${path}" >> hadoop_backup_status_${backup_date}.txt 
    
    hadoop distcp ${path} s3a://${s3_path}/${backup_date}/ > .garbarge_count 2>&1

    if [[ -z $(cat .garbarge_count  | grep -A4 'DistCp Counters' | grep 'DIR_COPY' | cut -d= -f2) ]]
    then 
        s3DirCopiedCount=0
    else
        s3DirCopiedCount=$(cat .garbarge_count  | grep -A4 'DistCp Counters' | grep 'DIR_COPY' | cut -d= -f2)
    fi

    if [[ -z $(cat .garbarge_count  | grep -A4 'DistCp Counters' | grep 'Files Copied' | cut -d= -f2) ]]
    then 
        s3FileCopiedCount=0
    else
        s3FileCopiedCount=$(cat .garbarge_count  | grep -A4 'DistCp Counters' | grep 'Files Copied' | cut -d= -f2)
    fi

    if [[ -z $(cat .garbarge_count  | grep -A4 'DistCp Counters' | grep 'Files Skipped' | cut -d= -f2) ]]
    then 
        s3FileSkippedCount=0
    else
        s3FileSkippedCount=$(cat .garbarge_count  | grep -A4 'DistCp Counters' | grep 'Files Skipped' | cut -d= -f2)
    fi

    hdfsFileCount=0
    for fileInHdfs in $(hdfs dfs -ls -R ${path} | grep 'part-' | awk '{print $8}')
    do
        hdfsFileCount=$((hdfsFileCount+1))
    done

    echo -e "Backup status:\nDirectories copied to s3: ${s3DirCopiedCount}\nFile copied to s3: ${s3FileCopiedCount}\nFile skipped: ${s3FileSkippedCount}\nFile in HDFS: ${hdfsFileCount}\n##############\n" >> hadoop_backup_status_${backup_date}.txt
done
rm -rf .garbarge_count

echo -e "\n######################\nCopy backup status file to hdfs and s3\n"

hdfs dfs -ls /backup_status
if [[ $? -eq 0 ]]; then echo test; else hdfs dfs -mkdir /backup_status; fi
hdfs dfs -put hadoop_backup_status_${backup_date}.txt hdfs:///backup_status
hadoop distcp hdfs:///backup_status/hadoop_backup_status_${backup_date}.txt s3a://${s3_path}/${backup_date}/
echo -e "Backup file copied successfully.\n######################\n"
