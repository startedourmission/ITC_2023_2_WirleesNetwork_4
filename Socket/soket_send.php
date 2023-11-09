<?php
    error_reporting(E_ALL);

    $address = "접속할 IP";
    $port = 접속할 PORT;
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP); // TCP 통신용 소켓 생성

    if ($socket === false) {
        echo "socket_create() 실패! 이유: " . socket_strerror(socket_last_error()) . "\n";
        echo "<br>";
    } else {
        echo "socket 성공적으로 생성.\n";
        echo "<br>";
    }

    echo "다음 IP '$address' 와 Port '$port' 으로 접속중...";
    echo "<br>";

    // 소켓 연결 및 $result에 접속값 지정
    $result = socket_connect($socket, $address, $port);

    if ($result === false) {
        echo "socket_connect() 실패.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
        echo "<br>";
    } else {
        echo "다음 주소로 연결 성공 : $address.\n";
        echo "<br>";
    }

    $sendData = "웹 서버로 보낼 데이터";
    echo "서버로 보내는 메세지 : $sendData\n";

    # 실제로 소켓으로 보내는 명령어
    socket_write($socket, $sendData, strlen($sendData));

    # 소켓으로 부터 받은 REQUEST 정보를 $input에 지정
    $input = socket_read($socket, 1024) or die("Could not read from Socket\n");

    # REQUEST 정보 출력
    echo $input;

    # 소켓 클로즈
    socket_close($socket);
?>
