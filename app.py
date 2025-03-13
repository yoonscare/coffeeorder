<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>음료 메뉴</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #5D4037;
            --secondary-color: #8D6E63;
            --background-color: #FFF8E1;
            --button-color-1: #90CAF9;
            --button-color-2: #CE93D8;
            --text-color: #212121;
            --border-radius: 12px;
        }
        
        body {
            font-family: 'Noto Sans KR', sans-serif;
            background-color: var(--background-color);
            margin: 0;
            padding: 20px;
            color: var(--text-color);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: var(--border-radius);
            padding: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        }
        
        .header {
            display: flex;
            align-items: center;
            margin-bottom: 30px;
            border-bottom: 3px solid var(--primary-color);
            padding-bottom: 15px;
        }
        
        .header-icon {
            background-color: var(--primary-color);
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 20px;
            font-size: 24px;
        }
        
        .title {
            font-size: 40px;
            font-weight: 900;
            color: var(--primary-color);
            margin: 0;
            display: flex;
            align-items: center;
        }
        
        .title .emoji {
            margin-left: 10px;
            font-size: 36px;
        }
        
        .options-row {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .option-button {
            flex: 1;
            padding: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: 700;
            border-radius: var(--border-radius);
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            background: linear-gradient(45deg, var(--button-color-1), var(--button-color-2));
            color: var(--text-color);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }
        
        .option-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        
        .input-row {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .input-field {
            flex: 1;
            padding: 15px;
            font-size: 18px;
            border: 2px solid var(--secondary-color);
            border-radius: var(--border-radius);
            background-color: white;
        }
        
        .input-field:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(93, 64, 55, 0.25);
        }
        
        .counter {
            display: flex;
            align-items: center;
            background-color: #212121;
            color: white;
            border-radius: var(--border-radius);
            overflow: hidden;
            margin-bottom: 20px;
        }
        
        .counter-value {
            padding: 15px 20px;
            font-size: 20px;
            font-weight: 700;
            flex: 1;
            text-align: center;
        }
        
        .counter-button {
            padding: 15px 20px;
            font-size: 24px;
            background-color: #111111;
            cursor: pointer;
            user-select: none;
            transition: background-color 0.2s;
        }
        
        .counter-button:hover {
            background-color: #333333;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-icon">☕</div>
            <h1 class="title">음료 메뉴 <span class="emoji">🍵🧋🥤</span></h1>
        </div>
        
        <div class="options-row">
            <div class="option-button">커피 선택 ☕</div>
            <div class="option-button">맞춤 옵션 🍶</div>
        </div>
        
        <div class="input-row">
            <input type="text" class="input-field" placeholder="음료를 검색하세요">
            <input type="text" class="input-field" placeholder="옵션을 검색하세요">
        </div>
        
        <div class="input-row">
            <input type="text" class="input-field" placeholder="선택한 음료">
            <input type="text" class="input-field" placeholder="선택한 옵션">
        </div>
        
        <div class="counter">
            <div class="counter-button">−</div>
            <div class="counter-value">1</div>
            <div class="counter-button">+</div>
        </div>
        
        <div class="input-row">
            <input type="text" class="input-field" placeholder="요청 사항을 입력하세요">
        </div>
    </div>
</body>
</html>
