from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()
    items = data.get("items", [])
    
    if not items:
        return jsonify({"error": "empty cart"}), 400
    
    # 验证商品数据格式
    for item in items:
        if "price" not in item or "quantity" not in item:
            return jsonify({"error": "invalid item format"}), 400
        if item["price"] < 0 or item["quantity"] < 1:
            return jsonify({"error": "invalid price or quantity"}), 400
    
    total = sum(i["price"] * i["quantity"] for i in items)
    
    # 添加运费逻辑
    shipping = 10 if total < 100 else 0
    final_total = total + shipping
    
    return jsonify({
        "total": total,
        "shipping": shipping,
        "final_total": final_total,
        "status": "success"
    }), 200

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
