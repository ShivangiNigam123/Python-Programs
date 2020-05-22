import speedtest
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(" Download Speed : ", download)
print("upload speed : ", upload)
