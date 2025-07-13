from django.shortcuts import render

def temperature_article(request):
    """View for Temperature & Heat Index article"""
    article_data = {
        'title': 'Temperature & Heat Index: Staying Safe in Extreme Temperatures',
        'icon': '🌡️',
        'intro': 'Understanding temperature variations and heat index is crucial for maintaining your health and comfort throughout the day. The heat index combines air temperature and relative humidity to determine how hot it actually feels to your body.',
        'sections': [
            {
                'title': 'Hot Weather Tips',
                'content': 'When temperatures soar above 85°F (29°C), your body works harder to maintain its normal temperature. Wear lightweight, light-colored, and loose-fitting clothing made from breathable fabrics like cotton or moisture-wicking materials. Schedule outdoor activities during cooler parts of the day - early morning or evening hours are ideal. Stay hydrated by drinking water regularly, even if you don\'t feel thirsty. Avoid caffeine and alcohol as they can contribute to dehydration. If you must be outside during peak heat hours, take frequent breaks in shaded or air-conditioned areas.'
            },
            {
                'title': 'Cold Weather Preparation',
                'content': 'When temperatures drop below 50°F (10°C), layering becomes essential. Start with a moisture-wicking base layer, add an insulating middle layer like fleece or wool, and finish with a waterproof outer shell. Don\'t forget accessories - hats, gloves, and scarves prevent significant heat loss. Watch for signs of hypothermia including shivering, confusion, and drowsiness. Keep your home heated to at least 68°F (20°C) and ensure proper insulation around windows and doors.'
            },
            {
                'title': 'Heat Index Awareness',
                'content': 'When the heat index exceeds 90°F (32°C), heat exhaustion becomes a real concern. Symptoms include heavy sweating, weakness, nausea, and headache. Move to a cool area immediately, apply cool water to skin, and seek medical attention if symptoms worsen. Remember that certain medications, age, and health conditions can affect your body\'s ability to regulate temperature. Always consult with healthcare providers about weather-related health concerns.'
            }
        ]
    }
    return render(request, 'article.html', {'article': article_data})

def precipitation_article(request):
    """View for Rain & Snow Forecasts article"""
    article_data = {
        'title': 'Rain & Snow Forecasts: Navigating Wet Weather Safely',
        'icon': '🌧️',
        'intro': 'Precipitation significantly impacts daily activities, from commuting to outdoor plans. Understanding rain and snow patterns helps you prepare effectively and stay safe during wet weather conditions.',
        'sections': [
            {
                'title': 'Rainy Day Strategies',
                'content': 'Check hourly forecasts to time outdoor activities between showers. Invest in quality rain gear including waterproof jackets, pants, and footwear with good traction. Keep a compact umbrella in your car, bag, or office for unexpected downpours. When driving in rain, reduce speed and increase following distance. Turn on headlights even during light rain to improve visibility. Avoid driving through flooded areas - just six inches of moving water can knock you down, and twelve inches can carry away a vehicle.'
            },
            {
                'title': 'Indoor Alternatives',
                'content': 'Plan backup indoor activities for rainy days. Visit museums, libraries, shopping centers, or enjoy home-based hobbies. Use rainy weather as an opportunity to tackle indoor projects, organize spaces, or try new recipes.'
            },
            {
                'title': 'Snow Preparation',
                'content': 'Winter storms require advance preparation. Stock up on essentials including food, water, medications, and flashlights. Ensure your vehicle has snow tires or chains, an emergency kit, and a full gas tank before storms arrive.'
            },
            {
                'title': 'Safe Snow Removal',
                'content': 'When shoveling snow, warm up with light exercises first. Push snow instead of lifting when possible, and take frequent breaks. Dress in layers and stay hydrated. Consider hiring professionals for heavy snowfall or if you have health concerns.'
            },
            {
                'title': 'Flooding Awareness',
                'content': 'Monitor flood warnings and avoid walking or driving through flood waters. Just two feet of rushing water can carry away vehicles. If trapped in a vehicle by flooding, abandon it and move to higher ground immediately. Create an emergency kit including battery-powered radio, first aid supplies, and important documents in waterproof containers.'
            }
        ]
    }
    return render(request, 'article.html', {'article': article_data})

def wind_article(request):
    """View for Wind Speed & Direction article"""
    article_data = {
        'title': 'Wind Speed & Direction: Adapting to Windy Conditions',
        'icon': '💨',
        'intro': 'Wind affects everything from outdoor activities to home safety. Understanding wind patterns and speeds helps you make informed decisions about daily plans and necessary precautions.',
        'sections': [
            {
                'title': 'Wind Speed Guidelines',
                'content': 'Light winds (0-15 mph) are generally pleasant for most activities. Moderate winds (16-25 mph) may affect outdoor dining and make cycling more challenging. Strong winds (26-35 mph) can make walking difficult and blow around loose objects. When winds exceed 35 mph, avoid outdoor activities near trees, power lines, or tall structures. Winds over 50 mph can cause significant property damage and create dangerous conditions for everyone.'
            },
            {
                'title': 'Outdoor Activity Adjustments',
                'content': 'For cyclists, headwinds require more effort while tailwinds provide assistance. Plan routes considering wind direction, and avoid cycling in crosswinds exceeding 20 mph. Runners should start runs against the wind when possible, finishing with wind assistance when fatigue sets in.'
            },
            {
                'title': 'Home and Garden Precautions',
                'content': 'Secure or store outdoor furniture, decorations, and garden tools before strong winds arrive. Trim tree branches near your home and remove dead or weak limbs that could fall. Check and secure loose roof tiles, gutters, and outdoor structures.'
            },
            {
                'title': 'Driving in Windy Conditions',
                'content': 'High-profile vehicles including trucks, RVs, and cars with roof cargo are most affected by strong winds. Reduce speed and maintain firm grip on the steering wheel. Be especially cautious on bridges, overpasses, and open highways where winds are typically stronger.'
            },
            {
                'title': 'Wind Chill Considerations',
                'content': 'Cold temperatures combined with wind create dangerous wind chill effects. When wind chill temperatures drop below 0°F (-18°C), exposed skin can develop frostbite within 30 minutes. Cover all exposed skin and limit outdoor exposure time.'
            }
        ]
    }
    return render(request, 'article.html', {'article': article_data})

def uv_article(request):
    """View for UV Index & Sun Protection article"""
    article_data = {
        'title': 'UV Index & Sun Protection: Safeguarding Your Skin',
        'icon': '☀️',
        'intro': 'The UV Index measures the strength of ultraviolet radiation from the sun, helping you protect your skin from harmful effects. Understanding UV levels enables you to enjoy outdoor activities safely while minimizing skin damage and cancer risk.',
        'sections': [
            {
                'title': 'UV Index Scale Understanding',
                'content': 'UV Index 0-2 (Low): Minimal protection needed for most people. UV Index 3-5 (Moderate): Seek shade during midday hours, wear protective clothing and sunscreen. UV Index 6-7 (High): Protection essential. UV Index 8-10 (Very High): Extra precautions necessary. UV Index 11+ (Extreme): Avoid outdoor activities during peak hours.'
            },
            {
                'title': 'Essential Sun Protection',
                'content': 'Apply broad-spectrum sunscreen with SPF 30 or higher to all exposed skin 15-30 minutes before going outdoors. Reapply every two hours, or after swimming, sweating, or toweling off. Don\'t forget often-missed areas like ears, neck, feet, and the back of hands.'
            },
            {
                'title': 'Protective Clothing Choices',
                'content': 'Wear long-sleeved shirts, pants, and wide-brimmed hats when possible. Dark colors and tightly woven fabrics provide better protection than light colors and loose weaves. Consider clothing with UPF (Ultraviolet Protection Factor) ratings for maximum protection.'
            },
            {
                'title': 'Timing Your Activities',
                'content': 'UV radiation is strongest between 10 AM and 4 PM. Plan outdoor activities during early morning or late afternoon when UV levels are lower. Use the shadow rule: if your shadow is shorter than you are, UV rays are at their strongest.'
            },
            {
                'title': 'Eye Protection',
                'content': 'Wear sunglasses that block 99-100% of UV-A and UV-B rays. Wraparound styles provide the best protection by preventing UV rays from entering around the sides. Prolonged UV exposure can cause cataracts and other eye problems.'
            },
            {
                'title': 'Special Considerations',
                'content': 'Snow, water, and sand reflect UV rays, increasing exposure by up to 15%. Higher altitudes mean stronger UV radiation - UV levels increase by 4% for every 1,000 feet of elevation. Cloudy days still require protection as up to 80% of UV rays can penetrate clouds.'
            }
        ]
    }
    return render(request, 'article.html', {'article': article_data})
