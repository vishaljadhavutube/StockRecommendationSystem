from flask import Blueprint, render_template
from app.models.models import db, Recommendation, Stock
from datetime import date

recommendations_bp = Blueprint("recommendations", __name__)

@recommendations_bp.route("/")
def index():
    today = date.today()
    recs = db.session.query(Recommendation, Stock).join(Stock).filter(Recommendation.date == today).all()
    return render_template("index.html", recommendations=[{
        "symbol": s.symbol,
        "entry_price": r.entry_price,
        "target_price": r.target_price,
        "holding_days": r.holding_days,
        "confidence_score": r.confidence_score
    } for r, s in recs])