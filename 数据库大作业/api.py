from flask import Flask, request, jsonify
import pymysql  # 或者你使用的数据库驱动
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# 第一个 API 端点
@app.route('/api/showFlights', methods=['GET'])
def showFlights():
    # 从请求中获取数据
    # data = request.get_json()

    # 连接数据库，处理数据
    connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
    cursor = connection.cursor()

    # 执行数据库操作，查询
    cursor.execute(f"SELECT * FROM Flights")
    result = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    connection.close()

    # 返回处理后的数据
    return jsonify(result)

# 第二个 API 端点
@app.route('/api/showHotels', methods=['GET'])
def showHotels():
    # 从请求中获取数据
    # data = request.get_json()

    # 连接数据库，处理数据
    connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
    cursor = connection.cursor()

    # 执行数据库操作，查询
    cursor.execute(f"SELECT * FROM hotels")
    result = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    connection.close()

    # 返回处理后的数据
    return jsonify(result)

# 第三个 API 端点
@app.route('/api/showBus', methods=['GET'])
def showBus():
    # 从请求中获取数据
    # data = request.get_json()

    # 连接数据库，处理数据
    connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
    cursor = connection.cursor()

    # 执行数据库操作，查询
    cursor.execute(f"SELECT * FROM bus")
    result = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    connection.close()

    # 返回处理后的数据
    return jsonify(result)

@app.route('/api/showCus', methods=['GET'])
def showCus():
    # 从请求中获取数据
    # data = request.get_json()

    # 连接数据库，处理数据
    connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
    cursor = connection.cursor()

    # 执行数据库操作，查询
    cursor.execute(f"SELECT * FROM customers")
    result = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    connection.close()

    # 返回处理后的数据
    return jsonify(result)

@app.route('/api/showRes', methods=['GET'])
def showRes():
    # 从请求中获取数据
    # data = request.get_json()

    # 连接数据库，处理数据
    connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
    cursor = connection.cursor()

    # 执行数据库操作，查询
    cursor.execute(f"SELECT * FROM reservations")
    result = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    connection.close()

    # 返回处理后的数据
    return jsonify(result)

@app.route('/api/checkRes', methods=['POST'])
def checkRes():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        checkRes_query = "SELECT checkRes(%s, %s, %s) AS Result;"
        cursor.execute(checkRes_query, (data['cusName'], data['fromCity'], data['arivCity']))
        connection.commit()
        
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        print("Received data:", data)
        print(result)
        print(jsonify(result))
        # 返回响应给客户端
        return jsonify(result),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500

@app.route('/api/onSubmitRes', methods=['POST'])
def onSubmitRes():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        insert_query = "INSERT INTO RESERVATIONS (custName, resvType, resvKey) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (data['cusName'], data['resType'], data['resKey']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500
    

@app.route('/api/onSubmitFlightsInsert', methods=['POST'])
def onSubmitFlightsInsert():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        insert_query = "INSERT INTO Flights (flightNum, price, numSeats, numAvail, fromCity, arivCity) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (data['flightNum'], data['price'], data['numSeats'], data['numAvail'], data['fromCity'], data['arivCity']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500
    
@app.route('/api/onSubmitHotelsInsert', methods=['POST'])
def onSubmitHotelsInsert():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        insert_query = "INSERT INTO Hotels (location, price, numRooms, numAvail) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (data['location'], data['price'], data['numRooms'], data['numAvail']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500
    

@app.route('/api/onSubmitBusInsert', methods=['POST'])
def onSubmitBusInsert():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        insert_query = "INSERT INTO Bus (location, price, numBus, numAvail) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (data['location'], data['price'], data['numBus'], data['numAvail']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500
    
@app.route('/api/onSubmitCusInsert', methods=['POST'])
def onSubmitCusInsert():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        insert_query = "INSERT INTO Customers (cusID, cusName) VALUES (%s, %s)"
        cursor.execute(insert_query, (data['cusID'], data['cusName']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500


@app.route('/api/onSubmitFlightsUpdate', methods=['POST'])
def onSubmitFlightsUpdate():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        update_query = "UPDATE Flights SET price = %s, numSeats = %s, numAvail = %s, fromCity = %s, arivCity = %s WHERE flightNum = %s"
        cursor.execute(update_query, (data['price'], data['numSeats'], data['numAvail'], data['fromCity'], data['arivCity'],data['flightNum']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500

@app.route('/api/onSubmitHotelsUpdate', methods=['POST'])
def onSubmitHotelsUpdate():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        update_query = "UPDATE Hotels SET price = %s, numRooms = %s, numAvail = %s WHERE location = %s"
        cursor.execute(update_query, (data['price'], data['numRooms'], data['numAvail'], data['location']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500
    
@app.route('/api/onSubmitBusUpdate', methods=['POST'])
def onSubmitBusUpdate():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        update_query = "UPDATE Bus SET price = %s, numBus = %s, numAvail = %s WHERE location = %s"
        cursor.execute(update_query, (data['price'], data['numBus'], data['numAvail'], data['location']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500
    
@app.route('/api/onSubmitCusUpdate', methods=['POST'])
def onSubmitCusUpdate():
    # 从请求中获取JSON数据
    try:

        data = request.get_json()

        connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='1119', database='travelDB')
        cursor = connection.cursor()

        update_query = "UPDATE Customers SET cusName = %s WHERE cusID = %s"
        cursor.execute(update_query, (data['cusName'], data['cusID']))
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Received data:", data)

        # 返回响应给客户端
        return jsonify({"message": "Data received successfully!"}),200
    
    except Exception as e:
        print("Received data:", data)
        return jsonify({"error": str(e)}),500
# ... 添加更多 API 端点

if __name__ == '__main__':
    app.run(port=5000)
