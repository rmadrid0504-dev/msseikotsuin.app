import React, { useState, useMemo } from 'react';
import { Calendar, CheckCircle, Users, Activity, ChevronRight, Star, Zap, Sparkles, MapPin, Plus } from 'lucide-react';

// ==========================================
// 🎨 ブランド・店舗設定 (ここで外観を調整)
// ==========================================
const BRAND_CONFIG = {
  name: "久留米まつもと整骨院", // 院名
  subTitle: "最適プラン診断ツール", // サブタイトル
  // テーマカラー設定 (blue, teal, green, rose, violet, amber から選択)
  themeColor: "amber", 
};

// ==========================================
// 📋 メニューデータ
// ==========================================
const MENU_DATA = {
  "根本改善コース（完全自費）": {
    single: 4400,
    tickets: { 5: 21000, 10: 38000, 20: 70000, 30: 96000 }
  },
  "根本改善コース（保険併用）": {
    single: 3300,
    tickets: { 5: 15250, 10: 28000, 20: 50000, 30: 66000, 40: 80000, 60: 99000 }
  },
  "EMSトレーニング": {
    single: 3300,
    tickets: { 5: 12500, 10: 22000, 20: 38000, 30: 52800 }
  },
  "鍼灸": {
    single: 2500,
    tickets: { 5: 12000, 10: 22000, 20: 40000, 30: 54000 }
  },
  "美容鍼コース": {
    single: 6600,
    tickets: { 5: 31500, 10: 60000, 20: 100000, 30: 120000 }
  }
};

// カラーパレット定義
const THEMES = {
  blue: { bg: "bg-blue-600", light: "bg-blue-50", text: "text-blue-600", border: "border-blue-200", ring: "focus:ring-blue-500", gradient: "from-blue-600 to-blue-500" },
  teal: { bg: "bg-teal-600", light: "bg-teal-50", text: "text-teal-700", border: "border-teal-200", ring: "focus:ring-teal-500", gradient: "from-teal-600 to-teal-500" },
  green: { bg: "bg-emerald-600", light: "bg-emerald-50", text: "text-emerald-700", border: "border-emerald-200", ring: "focus:ring-emerald-500", gradient: "from-emerald-600 to-emerald-500" },
  rose: { bg: "bg-rose-500", light: "bg-rose-50", text: "text-rose-600", border: "border-rose-200", ring: "focus:ring-rose-500", gradient: "from-rose-500 to-rose-400" },
  amber: { bg: "bg-amber-500", light: "bg-amber-50", text: "text-amber-700", border: "border-amber-200", ring: "focus:ring-amber-500", gradient: "from-amber-500 to-amber-400" },
};

export default function App() {
  const theme = THEMES[BRAND_CONFIG.themeColor] || THEMES.teal;
  
  const [selectedMenuKey, setSelectedMenuKey] = useState("根本改善コース（完全自費）");
  const [numPeople, setNumPeople] = useState(1);
  const [targets, setTargets] = useState([15, 10, 10, 10]); 

  const currentCourse = MENU_DATA[selectedMenuKey];

  // メッセージの出し分け
  const recommendedMessage = selectedMenuKey.includes("美容鍼") 
    ? "肌質改善の目安は10〜20回です" 
    : "機能改善の推奨は20~30回です";

  // メニューに応じたアイコンの取得
  const getMenuIcon = (menuName) => {
    if (menuName.includes("EMS")) return <Zap className={`w-5 h-5 ${theme.text}`} />;
    if (menuName.includes("美容")) return <Sparkles className={`w-5 h-5 ${theme.text}`} />;
    if (menuName.includes("鍼")) return <MapPin className={`w-5 h-5 ${theme.text}`} />;
    return <Activity className={`w-5 h-5 ${theme.text}`} />;
  };

  const currentIcon = getMenuIcon(selectedMenuKey);

  const totalTarget = useMemo(() => {
    let sum = 0;
    for (let i = 0; i < numPeople; i++) {
      sum += targets[i];
    }
    return sum;
  }, [numPeople, targets]);

  const suggestedCount = useMemo(() => {
    const counts = Object.keys(currentCourse.tickets).map(Number).sort((a, b) => a - b);
    const found = counts.find(c => c >= totalTarget);
    return found || counts[counts.length - 1];
  }, [totalTarget, currentCourse]);

  const limitDate = new Date();
  limitDate.setDate(limitDate.getDate() + 180);
  const formattedDate = `${limitDate.getFullYear()}年${limitDate.getMonth() + 1}月${limitDate.getDate()}日`;

  const handleTargetChange = (index, value) => {
    const newTargets = [...targets];
    newTargets[index] = Number(value);
    setTargets(newTargets);
  };

  return (
    // font-sans に戻してスッキリとした印象に
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 pb-20">
      <div className="max-w-md mx-auto bg-white shadow-2xl min-h-screen sm:min-h-0 sm:rounded-3xl sm:my-8 overflow-hidden border border-slate-100">
        
        {/* ヘッダーエリア */}
        <div className={`bg-gradient-to-br ${theme.gradient} p-8 text-white text-center shadow-lg relative overflow-hidden`}>
          {/* 背景装飾：医療十字と波形で整骨院らしさを表現 */}
          <div className="absolute top-0 left-0 w-full h-full opacity-10 pointer-events-none">
            <Activity className="absolute -top-4 -right-4 w-32 h-32" />
            <Plus className="absolute bottom-4 left-4 w-16 h-16" />
            <Plus className="absolute top-10 left-10 w-8 h-8" />
          </div>
          
          <div className="relative z-10">
            <h1 className="text-2xl font-bold tracking-wider mb-2 drop-shadow-md">{BRAND_CONFIG.name}</h1>
            <div className="inline-block bg-white/20 backdrop-blur-sm px-4 py-1 rounded-full border border-white/30">
              <p className="text-xs font-medium tracking-widest text-white">{BRAND_CONFIG.subTitle}</p>
            </div>
          </div>
        </div>

        <div className="p-6 space-y-8">
          
          {/* 1. メニュー選択 */}
          <div className="space-y-3">
            <label className="flex items-center gap-2 text-sm font-bold text-slate-600 uppercase tracking-wide">
              {currentIcon} {/* 選択されたメニューのアイコンを表示 */}
              診断コース
            </label>
            <div className="relative group">
              <select 
                value={selectedMenuKey}
                onChange={(e) => setSelectedMenuKey(e.target.value)}
                className={`block w-full p-4 pl-4 pr-10 border border-slate-200 rounded-xl bg-slate-50 ${theme.ring} focus:outline-none appearance-none font-bold text-lg text-slate-700 shadow-sm transition-all hover:border-slate-300`}
              >
                {Object.keys(MENU_DATA).map((key) => (
                  <option key={key} value={key}>{key}</option>
                ))}
              </select>
              <div className="absolute inset-y-0 right-0 flex items-center px-4 pointer-events-none text-slate-500">
                <ChevronRight className="w-5 h-5 rotate-90" />
              </div>
            </div>
          </div>

          {/* 2. 共有シミュレーション */}
          <div className="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
            <div className={`${theme.light} px-5 py-3 border-b ${theme.border} flex items-center justify-between`}>
              <div className="flex items-center gap-2">
                <Users className={`w-5 h-5 ${theme.text}`} />
                <h2 className={`font-bold ${theme.text}`}>共有シミュレーション</h2>
              </div>
              <span className="text-[10px] bg-white px-2 py-0.5 rounded-md border border-slate-200 text-slate-500 font-medium">親戚・カップルOK</span>
            </div>
            
            <div className="p-5 space-y-6">
              <div>
                <div className="flex justify-between items-center mb-4">
                  <label className="text-sm font-semibold text-slate-700">ご利用人数</label>
                  <span className={`text-lg font-bold ${theme.text} bg-white px-3 py-0.5 rounded-lg border ${theme.border}`}>{numPeople}名</span>
                </div>
                <input 
                  type="range" 
                  min="1" 
                  max="4" 
                  value={numPeople} 
                  onChange={(e) => setNumPeople(Number(e.target.value))}
                  className={`w-full h-2 rounded-lg appearance-none cursor-pointer bg-slate-200 accent-${BRAND_CONFIG.themeColor}-600`}
                  style={{ accentColor: theme.bg.replace('bg-', '').replace('-600', '') }} 
                />
              </div>

              <div className="space-y-3 bg-slate-50 p-4 rounded-xl border border-slate-100">
                {Array.from({ length: numPeople }).map((_, i) => (
                  <div key={i} className="flex flex-col">
                    <div className="flex justify-between items-baseline mb-1">
                      <label className="text-xs font-bold text-slate-500">
                        {i + 1}人目の目標回数
                      </label>
                      <span className="text-xs font-medium text-slate-400">現在: {targets[i]}回</span>
                    </div>
                    <input 
                      type="number"
                      min="1"
                      max="60"
                      value={targets[i]}
                      onChange={(e) => handleTargetChange(i, e.target.value)}
                      className={`p-2 border border-slate-200 rounded-lg w-full ${theme.ring} focus:outline-none text-center font-bold text-slate-700 shadow-sm`}
                    />
                    {i === 0 && <span className={`text-[10px] ${theme.text} mt-1.5 flex items-center gap-1 font-medium`}>
                      <Activity className="w-3 h-3" /> {recommendedMessage}
                    </span>}
                  </div>
                ))}
              </div>

              <div className="bg-slate-800 text-white p-4 rounded-xl flex items-center justify-between shadow-md">
                <span className="text-sm font-medium opacity-80">合計必要回数</span>
                <span className="text-2xl font-bold tracking-tight">{totalTarget} <span className="text-sm font-normal">回</span></span>
              </div>
            </div>
          </div>

          {/* 3. 価格一覧 */}
          <div className="space-y-4">
            <h2 className="text-lg font-bold text-slate-700 flex items-center gap-2 px-1">
              <Star className="w-5 h-5 text-amber-400 fill-amber-400" />
              プラン診断結果
            </h2>

            <div className="space-y-4">
              {Object.entries(currentCourse.tickets).map(([countStr, price]) => {
                const count = Number(countStr);
                const isSuggested = count === suggestedCount;
                const perUnit = Math.floor(price / count);
                const saving = (currentCourse.single * count) - price;

                return (
                  <div 
                    key={count}
                    className={`relative p-5 rounded-2xl transition-all duration-300 ${
                      isSuggested 
                        ? 'border-2 border-amber-400 bg-amber-50 shadow-xl scale-[1.02] z-10 ring-4 ring-amber-100/50' 
                        : 'border border-slate-200 bg-white shadow-sm hover:shadow-md'
                    }`}
                  >
                    {isSuggested && (
                      <div className="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-gradient-to-r from-amber-500 to-orange-500 text-white text-xs font-bold px-6 py-1.5 rounded-full shadow-md flex items-center gap-1 min-w-max">
                        <Star className="w-3 h-3 fill-white" />
                        おすすめプラン
                      </div>
                    )}
                    
                    <div className="flex justify-between items-baseline mb-3 pt-1">
                      <h3 className={`text-lg font-bold ${isSuggested ? 'text-slate-800' : 'text-slate-600'}`}>
                        {count}回券
                      </h3>
                      <p className={`text-2xl font-bold tracking-tight ${isSuggested ? 'text-amber-600' : 'text-slate-700'}`}>
                        {price.toLocaleString()}<span className="text-xs text-slate-400 font-normal ml-1">円(税込)</span>
                      </p>
                    </div>

                    <div className="space-y-1.5 text-sm">
                      <div className="flex justify-between text-slate-500">
                        <span>1回あたり</span>
                        <span className="font-semibold text-slate-700">{perUnit.toLocaleString()}円</span>
                      </div>
                      <div className={`flex justify-between items-center font-bold px-2 py-1 rounded-lg ${isSuggested ? 'bg-white text-amber-600 border border-amber-100' : 'bg-slate-50 text-emerald-600'}`}>
                        <span className="text-xs opacity-90">都度払いよりお得</span>
                        <span>{saving.toLocaleString()}円</span>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* 4. 特典・期限 */}
          <div className="grid grid-cols-2 gap-3 pt-2">
            <div className={`bg-white p-4 rounded-2xl border border-slate-100 shadow-sm flex flex-col items-center justify-center text-center gap-2`}>
              <div className={`p-2 rounded-full ${theme.light}`}>
                <CheckCircle className={`w-5 h-5 ${theme.text}`} />
              </div>
              <span className="text-xs font-bold text-slate-600 leading-tight">AI姿勢分析<br/>毎回無料</span>
            </div>
            <div className={`bg-white p-4 rounded-2xl border border-slate-100 shadow-sm flex flex-col items-center justify-center text-center gap-2`}>
              <div className={`p-2 rounded-full ${theme.light}`}>
                <Users className={`w-5 h-5 ${theme.text}`} />
              </div>
              <span className="text-xs font-bold text-slate-600 leading-tight">家族・親戚<br/>共有OK</span>
            </div>
          </div>

          <div className="bg-slate-100 p-4 rounded-xl flex items-start gap-3 border border-slate-200">
            <Calendar className="text-slate-400 w-5 h-5 mt-0.5 flex-shrink-0" />
            <div>
              <p className="text-xs text-slate-500 font-bold mb-1 uppercase tracking-wider">有効期限の目安</p>
              <p className="text-sm text-slate-800 font-medium">
                本日開始の場合: <span className="font-bold border-b-2 border-slate-300 pb-0.5">{formattedDate}</span> まで
              </p>
              <p className="text-[10px] text-slate-400 mt-2">
                ※20回券以降は10回分ごとの更新制となります。<br/>
                ※有効期限は1回目のご利用日から計算されます。
              </p>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}