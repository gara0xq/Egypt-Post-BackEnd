from rest_framework import serializers
from .models import *

class FirstDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicesModel
        fields = '__all__'

    def create(self, validated_data):

        currentserial = validated_data.pop('serial', None)
        currentoffice = validated_data.pop('office', None)
        currentIp = validated_data.pop('ip', None)

        startsSerials = DevicesModuleModel.objects.values_list('serial', flat= True)
        
        offices_obj = OfficesModel.objects.filter(office=currentoffice)
        sector_obj = ""

        for serial in startsSerials:
            currentserial = currentserial.lower()
            serial = serial.lower()
            if not currentserial.startswith(serial):
                print(currentserial.startswith(serial))
                print(serial)
                print(currentserial)
                raise serializers.ValidationError("Serial Incorrect")
            else:
                devices_module_obj = DevicesModuleModel.objects.filter(serial=serial)
                break
            
        
        if not offices_obj:
            raise serializers.ValidationError("Office Incorrect")
        
        try:
            sector_obj = SectorModel.objects.filter(sector=offices_obj[0].sector)
        except:
            raise serializers.ValidationError("Error 404")

        device.InsertDevice(
            validated_data,
            sector_obj[0].governorate,
            offices_obj[0].sector,
            currentoffice,
            offices_obj[0].officeType,
            devices_module_obj[0].model,
            currentserial,
            devices_module_obj[0].date,
            devices_module_obj[0].status,
            devices_module_obj[0].ram,
            devices_module_obj[0].deviceType,
            sector_obj[0].sectorCode,
            offices_obj[0].numOfWindows,
            currentIp
        )
        return DevicesModel.objects.create(**validated_data)


class SecondDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicesModel
        fields = '__all__'

    def create(self, validated_data):
        currentserial = validated_data.pop('serial', None)
        currentoffice = validated_data.pop('office', None)
        currentIp = validated_data.pop('ip', None)
        currentDeviceType = validated_data.pop('deviceType', None)
        currentModel = validated_data.pop('model', None)

        devices_module_obj = DevicesModuleModel.objects.filter(model=currentModel)
        offices_obj = OfficesModel.objects.filter(office=currentoffice)
        sector_obj = ""


        if not devices_module_obj:
            raise serializers.ValidationError("Serial Incorrect")
        
        if not offices_obj:
            raise serializers.ValidationError("Office Incorrect")

        try:
            sector_obj = SectorModel.objects.filter(sector=offices_obj[0].sector)
        except:
            raise serializers.ValidationError("Error 404")

        device.InsertDevice(
            validated_data,
            sector_obj[0].governorate,
            offices_obj[0].sector,
            currentoffice,
            offices_obj[0].officeType,
            currentModel,
            currentserial,
            devices_module_obj[0].date,
            devices_module_obj[0].status,
            devices_module_obj[0].ram,
            currentDeviceType,
            sector_obj[0].sectorCode,
            offices_obj[0].numOfWindows,
            currentIp
        )
        
class OfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficesModel
        fields = '__all__'
        
class DevicesModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicesModuleModel
        fields = '__all__'
        
class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorModel
        fields = '__all__'

class device():
    def InsertDevice(
            validated_data,
            goverment,
            sector,
            office,
            officeType,
            model,
            serial,
            date,
            status,
            ram,
            deviceType,
            sectorCode,
            numOfWindows,
            ip
        ):
        
        validated_data['governorate'] = goverment
        validated_data['sector'] = sector
        validated_data['office'] = office
        validated_data['officeType'] = officeType
        validated_data['model'] = model
        validated_data['serial'] = serial
        validated_data['date'] = date
        validated_data['status'] = status
        validated_data['ram'] = ram
        validated_data['deviceType'] = deviceType    
        validated_data['sectorCode'] = sectorCode
        validated_data['numOfWindows'] = numOfWindows
        validated_data['ip'] = ip