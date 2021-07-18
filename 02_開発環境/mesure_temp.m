clear
% 近くにあるBluetooth Low Energy周辺デバイスのスキャン(5s間)
t_scan_advertise_struct = blelist("Timeout",10);
% 温湿度計のデバイスIDを取得
t_thermoHygrometer_id = "DB023921EECA";
% 温湿度計のデバイスに接続
t_thermoHygrometer = ble(t_thermoHygrometer_id);
% UUIDを取得
t_bot_serviceUUID               = "CBA20D00-224D-11E6-9FB8-0002A5D5C51B";    % 温湿度計のサービスUUID
t_data_characteristicUUID       = "CBA20003-224D-11E6-9FB8-0002A5D5C51B";    % データキャラクタリスティックUUID
t_command_characteristicUUID    = "CBA20002-224D-11E6-9FB8-0002A5D5C51B";    % コマンドキャラクタリスティックUUID

% characteristicオブジェクトを作成
c1 = characteristic(t_thermoHygrometer,t_bot_serviceUUID,t_command_characteristicUUID);
c10 = characteristic(t_thermoHygrometer,t_bot_serviceUUID,t_data_characteristicUUID);
% 通知の受信を開始
subscribe(c10);

% 10回計測する
for t_idx = 1:10
    write(c1, [0x57 0x0f 0x31], "withResponse");
    data = read(c10);
    humi = data(4)
    temp = str2double( bitand(data(3), 0b01111111) + "." + data(2) )
    pause(1);
end
return;