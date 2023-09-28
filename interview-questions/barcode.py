# company: amazon
# date: 24 Sept 2023
# platform: hackerrank
# ref: https://leetcode.com/discuss/interview-question/4096304/amazon-oa-sde-2
# question:  A barcode scanner can be configured by scanning a series of barcodes in the correct order. Barcode configurations are encoded into a single string and stored as a blob in the backend system. The client requests the configuration from the backend system, and then needs to present the configurations in the correct order. The encoded configuration string is a series of <ordinal-index><configuration> pairs separated by |. The ordinal index valid is a 4 digit numeric prefixed with zeros. For example, the first configuration will be represented as 0001

class Solution:
    def validateAndConfigure(self, s):
        configs = s.split("|")
        arr = [0 for i in range(len(configs) + 1)]
        lconfig = len(configs)

        for config in configs:
            if config == "":
                continue
            indx, mainConfig = int(config[0:4]), config[4:]

            if indx > lconfig:
                return ["Invalid"]
            if arr[indx]:
                return ["Invalid configuration"]
            
            arr[indx] = mainConfig

        arr.pop(0)
        return arr

sol = Solution()
ts = [
    "0001f7c22e7904|000176a3a4d214|000105d29f4a4b",
    "0001f7c22e7904|000276a3a4d214|000305d29f4a4b|000405d29f4a4b",
    "0002f7c22e7904|000376a3a4d214|000405d29f4a4b",
    "0002f7c22e7904|000376a3a4d214|000405d29f4a4b|"
]

for t in ts:
    print(sol.validateAndConfigure(t))
