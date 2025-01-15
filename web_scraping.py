import requests
from bs4 import BeautifulSoup
url = 'https://www.amazon.in/s?k=watches+for+woman&crid=3IQFM5DZXZE30&sprefix=watches%2Caps%2C238&ref=nb_sb_ss_ts-doa-p_2_7'
res = requests.get(url)
print(res)
soup = BeautifulSoup(res.content,'html.parser')

title = soup.title.text
body = soup.body.text

print(title)
print(body)


# import re
# text = """Live ScoresScheduleArchivesNewsAll Stories  Premium Editorials Latest NewsTopicsSpotlightOpinionsSpecialsStats & AnalysisInterviewsLive BlogsHarsha BhogleSeries 
# India tour of Australia, 2024-25 SA20, 2025 ICC Champions Trophy,
# 2025 West Indies tour of Pakistan, 2025 Big Bash League 2024-25 Sri Lanka tour of New Zealand, 2024-25 Vijay Hazare Trophy 2024-25 Bangladesh Premier League, 2024-25 Ireland Womens tour of India, 2025 All Series »Teams   Test Teams India Afghanistan Ireland Pakistan Australia Sri Lanka Bangladesh England West Indies South Africa Zimbabwe New Zealand   Associate Malaysia Nepal Germany Namibia Denmark Singapore Papua New Guinea Kuwait Vanuatu Jersey Oman Fiji   More... Videos  All Videos Categories Playlists   RankingsICC Rankings - MenICC Rankings - Women More World Test Championship World Cup Super League Auction Tracker Photos Mobile AppsCareersContact Us  {{premiumScreenName}}     My Account Sign Out MATCHESMLS vs SYS - LiveSEC vs MICT - PreviewRAJ vs TN - LiveHAR vs BEN - LiveWEL vs CD - CD WonAllLive NowTodayINTERNATIONALPakistan v West Indies, 2025Pakistan A vs West Indies2-day Warm-up MatchSL tour of NZ 2024-25New Zealand vs Sri Lanka2nd ODINew Zealand vs Sri Lanka3rd ODISouth Africa vs Pakistan,2024-25South Africa vs Pakistan2nd TestT20 LEAGUESA20Sunrisers Eastern Cape vs MI Cape Town1st MatchDurban Super Giants vs Pretoria Capitals2nd MatchBBL 2024-25Perth Scorchers vs Melbourne Renegades26th MatchSydney Thunder vs Hobart Hurricanes27th MatchMelbourne Stars vs Sydney Sixers  LIVE28th MatchHobart Hurricanes vs Sydney Thunder29th MatchSydney Sixers vs Perth Scorchers30th MatchAdelaide Strikers vs Brisbane Heat31st MatchBPL, 2024-25Dhaka Capitals vs Rangpur Riders11th MatchSylhet Strikers vs Fortune Barishal12th MatchFortune Barishal vs Rangpur Riders  LIVE13th MatchDhaka Capitals vs Chittagong Kings14th MatchDurbar Rajshahi vs Khulna Tigers15th MatchDhaka Capitals vs Sylhet Strikers16th MatchSuper Smash 2024-25Wellington vs Central Districts10th MatchCanterbury vs Auckland11th MatchDOMESTICVijay Hazare TrophyRajasthan vs Tamil Nadu  LIVE2nd Preliminary quarter finalHaryana vs Bengal  LIVE1st Preliminary quarter finalTBC vs TBC4th Preliminary quarter finalTBC vs TBC3rd Preliminary quarter finalWOMENIndia Women v Ireland Women, 2025India Women vs Ireland Women1st ODI (ICC Championship Match)        28th Match • Big Bash League 2024-25 T20   MLS154-5 (19.5) SYS Sydney Sixers opt to bowl       fantasy     table     schedule         1st Match • SA20, 2025 T20   Sunrisers Eastern Cape MI Cape Town         fantasy     table     schedule         2nd Preliminary quarter final • Vijay Hazare Trophy 2024-25 List A   RAJ267 (47.3) TN134-4 (25.1) Tamil Nadu need 134 runs       points table     schedule         1st Preliminary quarter final • Vijay Hazare Trophy 2024-25 List A   HAR298-9 (50) BEN104-2 (21) Bengal need 195 runs       points table     schedule         10th Match • Super Smash 2024-25 T20   WEL192-4 (20) CD196-4 (20) Central Districts won by 6 wkts       points table     schedule         13th Match • Bangladesh Premier League, 2024-25 T20   BRSA..197-5 (20) RGR28-1 (5.2) Rangpur Riders need 170 runs in 88 balls       points table     schedule           X   Quick Access     BGT 2024-25    Fantasy Handbook    See Plans    Team India    Cricbuzz Plus    CB Plus & Times Prime      LATEST NEWSSteve Smith to lead Australia in Sri Lanka8h agoOptimism around Shami's return; Akash Deep ruled out for a month17h agoGuptill retires from international cricket18h agoICC rates SCG pitch as 'satisfactory'1d agoYounis Khan to mentor Afghanistan at Champions Trophy 20251d agoOnly taking a break from Bangladesh national side, clarifies Jahanara Alam1d agoMominul voices concern over potential two-tier Test system1d agoBCCI shortlists WPL venues; Baroda likely to host the final1d agoI would've taken Shami to Australia - Ravi Shastri2d agoStats: Shan Masood leads Pakistan's herculean follow-on fightback2d agoMore News..  LATEST PHOTOS     Australia vs India, 5th Test, Day 3 Sun, Jan 05 2025      Australia vs India, 5th Test, Day 1 Fri, Jan 03 2025      Australia vs India, 4th Test, Day 5 Mon, Dec 30 2024      Australia vs India, 4th Test, Day 4 Sun, Dec 29 2024      Australia vs India, 4th Test, Day 3 Sat, Dec 28 2024      Australia vs India, 4th Test, Day 2 Fri, Dec 27 2024    More Photos..     SCHEDULE   Pakistan A vs West Indies, 2-day Warm-up Match, Day 1  •  GMT   New Zealand vs Sri Lanka, 3rd ODI  •  GMT   Pakistan A vs West Indies, 2-day Warm-up Match, Day 2  •  GMT   Pakistan vs West Indies, 1st Test, Day 1  •  GMT   Pakistan vs West Indies, 1st Test, Day 2  •  GMT   Pakistan vs West Indies, 1st Test, Day 3  •  GMT   Pakistan vs West Indies, 1st Test, Day 4  •  GMT   Pakistan vs West Indies, 1st Test, Day 5  •  GMT   India vs England, 1st T20I  •  GMT   India vs England, 2nd T20I  •  GMT   Pakistan vs West Indies, 2nd Test, Day 1  •  GMT   More Matches..       FITNESS UPDATE  Optimism around Shami's return; Akash Deep ruled out for a monthMeanwhile, Yuzvendra Chahal has been overlooked for Haryana's knockout matches in Vijay Hazare TrophySQUAD ANNOUNCEMENT       Steve Smith to lead Australia in Sri LankaCummins is on paternity leave while both the injured Hazlewood and out-of-form Mitchell Marsh also miss outBORDER GAVASKAR TROPHY, 2024-25 A contest headlined by two pace attacksBatters played false shots to 25.1% of the deliveries from seamers in the series - one in four deliveries - making it the toughest series for batters in Australia since 2006/07How Australia reclaimed the Border-Gavaskar TrophyIndia crack without lone warrior BumrahStats / Australia's first come-from-behind series win since 1997ICC rates SCG pitch as 'satisfactory'SHASTRI SPEAKS       I would've taken Shami to Australia - Ravi ShastriRicky Ponting too felt 'things could've been completely different' if India had Bumrah, Siraj and Shami in the playing XIBumrah rues missed opportunity of bowling on 'spiciest wicket of the series'Everything boils down to temperament: Gambhir on India's batting woesSA20, 2025     SA20 aims to be IPL's biggest little brotherHalf of the six teams in the UAE's ILT20, which clashes with the SA20, are IPL-owned. But, for SA20 commissioner Graeme Smith, the similarities stop thereSRI LANKA TOUR OF NEW ZEALAND, 2024-25 NZ demolish SL despite Theekshana's hattrickSri Lanka folded for 142 in their chase of 255 NEW ZEALAND CRICKETGuptill retires from international cricketThe opener represented New Zealand in 367 matches, scoring 13463 runs in international cricketWPL 2025      BCCI shortlists WPL venues; Baroda likely to host the finalLucknow in race to host a part of the 23-game two-phase league, expected to kick off in first week of February.BRIGHT FUTURE       Maphaka takes first steps on a long roadOn debut, Kwena Maphaka embraced the grind of Test cricket, balancing teenage nerves with raw talent to signal a promising bright futureLong day's journey to victory for South AfricaSouth Africa seal 10-wicket win to complete whitewashStats: Shan Masood leads Pakistan's herculean follow-on fightbackEXCLUSIVE INTERVIEWOnly taking a break from Bangladesh national side, clarifies Jahanara Alam1d agoThe ace Bangladesh pacer has also asked to be kept off the central contract list following her indefinite break from international cricket   Jahanara takes break from cricket due to mental health issuesAUS VS IND, 5TH TEST 'Stood down from SCG Test because runs weren't coming from my bat'Rohit Sharma also emphasized that this decision does not mean he's retiringUnpacking Rohit Sharma's omission from SCG TestRohit has shown leadership by opting out, says BumrahBIG BASH 2024-25    Renegades stay alive as they overcome Scorchers in Perth Will Sutherland and Tom Rogers led the visitors to victory after having fallen to 44/5 within 10 overs Bryant, Renshaw script turnaround to spoil Christian's returnLEGEND IN SERVICEYounis Khan to mentor Afghanistan at Champions Trophy 20251d agoThe former Pakistan captain will join the squad before the event in Pakistan & UAE TWO-TIER TEST SYSTEMMominul voices concern over potential two-tier Test system1d agoThe Bangladesh batter believes that teams in the second division will fail to improve if they do not compete with the top teams       Featured Videos3:07 ▶ Watching Bumrah bowl, the highlight of Australia tour: Harsha Bhogle2:24 ▶ Hope Gill's Test struggles don't cloud his ODI credentials: Dinesh Karthik2:09 ▶ India didn't play badly but failed to seize moments: Parthiv PatelMore Videos     Specials January 2025 - News DigestNews bytes that you may have missed otherwiseSacrifice over showcase: Behind Nitish Reddy's journey to India coloursThe all-rounder's rise to the top is defined by more than just accolades. His journey is a testament to sacrifice and dedication, shaped by his father's tough decisions and his family's quiet resilienceBen Stokes sees the finishing lineBen Stokes' place in a lineage of romanticised English talismans is secure, but the final acts in his international career still have the opportunity to define himBreaching Bastions: Young and the extraordinaryIn an exclusive interview, the Player of the Series in New Zealand's greatest Test series triumph reflects on the toils and tactics that got him hereMcSweeney and Doggett: The bond of brothers that transcended borders Story of two true-maroon Queensladers, who made the shift to South Australia together in search of higher reachesShakib's Test match legacy - one of the game's greatest all-roundersThe all-rounder played a strong part with both bat and ball during his Test careerHow the ICC academy bounced back from a desert floodWhen Dubai received the biggest downpour in recorded history in April, the most diversely equipped academy in world cricket was left to pick up the piecesJoe Root - England's Numero UnoSeveral batting records tumbled on Day 3 of the Multan Test where Root surpassed Cook to become England's highest Test run getterIndia's World Cup win wasn't a feeling, it was an emotionIt was the kind of emotion that cannot easily be explained. There was pure joy for sure. But there was also relief, and that bit of unexplained mania       We use cookies to improve your experience on our site and to show you non-personalized ads. Find out more in our privacy policy and cookie policyOKMOBILE SITE & APPSm.cricbuzz.comAndroidiOSFOLLOW US ONfacebooktwitteryoutubePinterestCOMPANYCareersAdvertisePrivacy PolicyTerms of UseCricbuzz TV AdsPrivacy Preferences© 2025 Cricbuzz.com, Times Internet Limited. All rights reserved | The Times of India | Navbharat TimesMove to top
# """
# xyz = r'\bAustralia\b|\bIndia\b'
# match = re.findall(xyz,text)
# print(len(match))



















# import re
# text = """Amazon.in Bestsellers: The most popular items on Amazon





























# Skip to



# Main content





#       Keyboard shortcuts






# Search

# alt
# +
# /







# Cart

# shift
# +
# alt
# +
# c







# Home

# shift
# +
# alt
# +
# h







# Orders

# shift
# +
# alt
# +
# o





# Show/hide shortcuts, shift, alt, z

# Show/Hide shortcuts

# shift
# +
# alt
# +
# z

















# .in









#                    Delivering to Mumbai 400001


#                    Update location





















# All


# Select the department you want to search in

# All Categories
# Alexa Skills
# Amazon Devices
# Amazon Fashion
# Amazon Fresh
# Amazon Fresh Meat
# Amazon Pharmacy
# Appliances
# Apps & Games
# Audible Audiobooks
# Baby
# Beauty
# Books
# Car & Motorbike
# Clothing & Accessories
# Collectibles
# Computers & Accessories
# Deals
# Electronics
# Furniture
# Garden & Outdoors
# Gift Cards
# Grocery & Gourmet Foods
# Health & Personal Care
# Home & Kitchen
# Industrial & Scientific
# Jewellery
# Kindle Store
# Luggage & Bags
# Luxury Beauty
# Movies & TV Shows
# MP3 Music
# Music
# Musical Instruments
# Office Products
# Pet Supplies
# Prime Video
# Shoes & Handbags
# Software
# Sports, Fitness & Outdoors
# Subscribe & Save
# Tools & Home Improvement
# Toys & Games
# Under ₹500
# Video Games
# Watches













# Search Amazon.in

























# EN





# Hello, sign in
# Account & Lists



# Returns
# & Orders










#         Cart













# All










# Fresh
# MX Player
# Sell
# Best Sellers
# Mobiles
# Today's Deals
# Prime
# Customer Service
#  Electronics
# Home & Kitchen
# Amazon Pay
# New Releases
# Fashion
# Computers
# Car & Motorbike
# Books
# Toys & Games
# Sports, Fitness & Outdoors
# Beauty & Personal Care
# Gift Cards
# Home Improvement
# Custom Products
# Health, Household & Personal Care
# Grocery & Gourmet Foods
# Video Games
# Baby
# Pet Supplies
# Audible
# Gift Ideas
# AmazonBasics
# Subscribe & Save
# Kindle eBooks






































# BestsellersHot New ReleasesMovers and ShakersMost Wished ForMost Gifted













# Amazon BestsellersOur most popular products based on sales.  Updated frequently.Bestsellers










# Any DepartmentAmazon LaunchpadAmazon RenewedApps for AndroidBaby ProductsBags, Wallets and LuggageBeautyBooksCar & MotorbikeClothing & AccessoriesComputers & AccessoriesElectronicsGarden & OutdoorsGift CardsGrocery & Gourmet FoodsHealth & Personal CareHome & KitchenHome ImprovementIndustrial & ScientificJewelleryKindle StoreMovies & TV ShowsMusicMusical InstrumentsOffice ProductsPet SuppliesShoes & HandbagsSoftwareSports, Fitness & OutdoorsToys & GamesVideo GamesWatches










#  Bestsellers in Industrial & ScientificSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1Konvio Neer Imported Tds Meter, Total Dissolved Solids Meter, Water Quality Tester, Ppm Tester For Water Testing - White4.3 out of 5 stars 45,027#2Daluci Anti Pollution N95 Reusable Unisex Non Woven fabric Face Mask, Ear Loop Style (Pack of 10) Protective Fold Flat Mask With 5 Layered Filtration, Without Valve3.9 out of 5 stars 10,512#3Dr Trust USA Compressor Nebulizer Machine Complete Kit for Adults and Kids with Mask (White)4.2 out of 5 stars 26,800#4Dr. Fixit Kwik N Ezee Wall Gap & Crack Filler, 150gm (White), DIY Waterproofing for Home Repairs, Kitchen Sink & Wall Cracks, Bathroom Tile Gaps Sealant, Metal, Wood, PVC, Best for Wet & Damp areas3.7 out of 5 stars 7,695#5REDCOP® Isopropyl Alcohol 99.9% Pure [(CH3)2-CH-OH] CAS: 67-63-0] 300ml Rubbing Alcohol4.3 out of 5 stars 2,428#6UB Unity Brand Super Strong Adhesive Waterproof tape Permanent Repair Roof Water Leakage Solution Rubber Foil Suitable for Roof Leak, surface Crack, Window Sill Gap, Boat Sealing, Tank Leak (5CM*5M)4.5 out of 5 stars 561Next page






#  Bestsellers in Grocery & Gourmet FoodsSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1Tata Salt 1 Kg, Free Flowing and Iodised Namak, Vacuum Evaporated, Salt in Fresh4.5 out of 5 stars 67,548#2Tata Sampann Unpolished Toor Dal/Arhar Dal, 1kg4.5 out of 5 stars 32,112#3Fortune Sunlite Refined Sunflower Oil, 1L4.4 out of 5 stars 37,205#4Fortune Premium Kachi Ghani Pure Mustard Oil, 1Litre PET Bottle4.4 out of 5 stars 45,943#5Amazon Brand - Vedaka Cumin (Safed Zeera) whole, 100 g4.4 out of 5 stars 28,157#6Fortune Premium Kachi Ghani Pure Mustard Oil, 1 ltr pouch4.4 out of 5 stars 32,163Next page






#  Bestsellers in Car & MotorbikeSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1SOFTSPUN Microfiber Cloth - 4 pcs - 40x40 cms - 340 GSM Grey! Thick Lint & Streak-Free Multipurpose Cloths - Automotive Microfibre Towels for Car Bike Cleaning Polishing Washing & Detailing.4.3 out of 5 stars 93,454#2Jopasu Car Duster4.4 out of 5 stars 40,111#3Godrej aer O – Hanging Car Air Freshener – Assorted Pack of 3 (22.5g) | Gel Lasts up to 30 days | Car Accessories4.2 out of 5 stars 1,926#4ShineXPro Microfiber Car Cleaning Cloth - OG Soft 500 GSM Extra Large (35x75 CM) Microfiber Cloth for Car and Bike - Suede Edging for Scratchless Drying and Detailing (Pack of 2, Grey)4.3 out of 5 stars 13,907#5Boldfit Full Face Helmet Mask for Bikers in Riding UV Protected, Balaclava, Black Mask for Bike Riding and Cycling Accessories Mask for Men & Women4.1 out of 5 stars 5,701#6Involve Your Senses One Musk Organic Car Perfume, Involve Your Senses Strong Fiber Air Freshener to Freshen'up Your Car - IONE01-40 g,Car Accessories interior car perfumes and fresheners3.8 out of 5 stars 26,768Next page






#  Bestsellers in Gift CardsSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1Google Play recharge code - Digital Voucher4.3 out of 5 stars 279,677#2Amazon Pay eGift Card4.5 out of 5 stars 205,722#3Amazon Pay eGift Card4.5 out of 5 stars 205,722#4Reliance Retail | Flat 3% off | E-Gift Card | Instant Delivery | Valid for in-store purchases |1 year Validity5.0 out of 5 stars 5#5Google Play Gift Card| 2% Flat Cashback | Instant Delivery | Valid for online purchase | Redeemable on Play Store4.1 out of 5 stars 143#6App Store Codes4.1 out of 5 stars 260Next page






#  Bestsellers in ElectronicsSee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1realme NARZO 70x 5G (Ice Blue, 6GB RAM,128GB Storage)|120Hz Ultra Smooth Display|Dimensity 6100+ 6nm 5G|50MP AI Camera|45W Charger in The Box4.1 out of 5 stars 4,365#2boAt Rockerz 255 Pro+, 60HRS Battery, Fast Charge, IPX7, Dual Pairing, Low Latency, Magnetic Earbuds, Bluetooth Neckband, Wireless with Mic Earphones (Active Black)4.0 out of 5 stars 206,013#3realme NARZO N61 (Voyage Blue,4GB RAM+64GB Storage) 90Hz Eye Comfort Display | IP54 Dust & Water Resistance | 48-Month Fluency | Charger in The Box4.0 out of 5 stars 1,456#4Apple 20W USB-C Power Adapter (for iPhone, iPad & AirPods)4.3 out of 5 stars 2,562#5Redmi A4 5G (Sparkle Purple, 4GB RAM, 128GB Storage) | Global Debut SD 4s Gen 2 | Segment Largest 6.88in 120Hz | 50MP Dual Camera | 18W Fast Charging4.0 out of 5 stars 581#6boAt Bassheads 100 in Ear Wired Earphones with Mic(Black)4.1 out of 5 stars 412,589Next page






#  Bestsellers in JewellerySee MorePage 1 of 1 Start overPage 1 of 1  Previous page#1Elina Dark Multi Color Elastic Hair Ponytail Holder Soft Non Slip Tight Stretchable Rubber Bands for School Girls/Women, Hair tie (Pack of 30)(Dark English Multicolor)4.4 out of 5 stars 692#2Shining Diva Fashion 26 Pcs Colorful Hair Accessories Hair Clips for Girls Kids Baby Girl Toddlers Women Hairband Hair Band Ties4.3 out of 5 stars 875#3Gold Plated Invisible Transparent Stretchable and Adjustable Lightweighted Elastic Heavy Earrings Support Ear Chains (2 Pair) And Invisible Ear Lobe Support for Earrings Earlobe Tapes and Stickers Earring Supporter for Heavy Earrings Support Patches Girls & Women (Pack 20)3.5 out of 5 stars 27#4JEWILLEY Floral Kundan Studded Matha Patti Sheesh Patti Wedding Hairband Traditional Golden Celebrity Headband Hair accessory Jewellery for Women and Girls4.3 out of 5 stars 101#5Zeneme Traditional Brass 18 K Gold Plated Wedding Jewellery Bahubali Inspired Long Chain Jhumki Earrings for Women and Girl4.1 out of 5 stars 300#6Shining Diva Fashion Latest Stylish Multilayer Gold Plated Bangle Bracelet for Women and Girls (rr14669b) Set of 63.5 out of 5 stars 540Next page







# About BestsellersThese frequently updated lists contain bestselling items.





























#                     Your recently viewed items and featured recommendations      ›    View or edit your browsing history     After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.         Your recently viewed items and featured recommendations      ›    View or edit your browsing history     After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.




#     Back to top






# Get to Know Us


# About Amazon


# Careers


# Press Releases


# Amazon Science





# Connect with Us


# Facebook


# Twitter


# Instagram





# Make Money with Us


# Sell on Amazon


# Sell under Amazon Accelerator


# Protect and Build Your Brand


# Amazon Global Selling


# Supply to Amazon


# Become an Affiliate


# Fulfilment by Amazon


# Advertise Your Products


# Amazon Pay on Merchants





# Let Us Help You


# Your Account


# Returns Centre


# Recalls and Product Safety Alerts


# 100% Purchase Protection


# Amazon App Download


# Help

















# English



# India






# AbeBooksBooks, art& collectibles
# Amazon Web ServicesScalable CloudComputing Services
# AudibleDownloadAudio Books
# IMDbMovies, TV& Celebrities
 

# ShopbopDesignerFashion Brands

# Amazon BusinessEverything ForYour Business
# Prime Now 2-Hour Deliveryon Everyday Items
# Amazon Prime Music100 million songs, ad-freeOver 15 million podcast episodes



# Conditions of Use & Sale Privacy Notice Interest-Based Ads © 1996-2025, Amazon.com, Inc. or its affiliates
# """
# xyz = r'[A-Za-z0-9]+[0-9]+'
# match = re.findall(xyz,text)
# print(match)

#########################################################################################################################################################################


